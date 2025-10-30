import re

class ViolinFingeringMap:
    CHROMATIC_SHARP = ['c', 'cis', 'd', 'dis', 'e', 'f', 'fis', 'g', 'gis', 'a', 'ais', 'b']
    CHROMATIC_FLAT = ['c', 'des', 'd', 'ees', 'e', 'f', 'ges', 'g', 'aes', 'a', 'bes', 'b']
    OCTAVE_MARKS = ["", "'", "''", "'''", "''''", "'''''", "''''''"]

    ENHARMONIC_MAP = {
        "ces": "b", "des": "cis", "ees": "dis", "fes": "e", "ges": "fis",
        "aes": "gis", "bes": "ais", "cis": "des", "dis": "ees", "eis": "f",
        "fis": "ges", "gis": "aes", "ais": "bes", "bis": "c"
    }

    STARTING_NOTES = {
        'G': 'g',
        'D': "d'",
        'A': "a'",
        'E': "e''"
    }

    POSITIONS = ['I', 'III']
    ALL_POSITIONS = [f'{i}' for i in ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X', 'XI', 'XII', 'XIII', 'XIV', 'XV']]

    def __init__(self, tonic='g', scale_type='major', octaves=3):
        self.tonic = tonic
        self.scale_type = scale_type
        self.octaves = octaves
        self.note_names = self._generate_note_names()
        self.current_scale = self._generate_scale()
        self.fingering_map = {}
        self.other_fingering_map = []

    def _generate_note_names(self):
        notes = []
        idx = self.CHROMATIC_SHARP.index('g')
        octave = 0
        for _ in range(self.octaves * 12):
            note = self.CHROMATIC_SHARP[idx % 12]
            if note == 'c':
                octave += 1
            notes.append(note + self.OCTAVE_MARKS[octave])
            idx += 1
        print(notes)
        return notes

    def _generate_scale(self):
        chromatic = self.CHROMATIC_SHARP if self.tonic in ["f", "bes", "ees", "aes", "des", "ges", "ces", "fes"] in self.CHROMATIC_FLAT else self.CHROMATIC_SHARP
        steps = [2, 2, 1, 2, 2, 2, 1] if self.scale_type == 'major' else [2, 1, 2, 2, 1, 2, 2]
        try:
            start_index = chromatic.index(self.tonic)
        except ValueError:
            raise ValueError(f"Tonic '{self.tonic}' not found in chromatic scale.")

        scale_notes = []
        idx = start_index
        octave = 0
        for _ in range(self.octaves):
            for step in steps:
                note = chromatic[idx % 12]
                if note == 'c':
                    octave += 1
                scale_notes.append(note + self.OCTAVE_MARKS[octave])
                print(idx, note)
                idx += step
        return set(scale_notes)

    def normalize(self, note):
        match = re.match(r"([a-g][ei]s|[a-g]es|[a-g])([',]*)$", note)
        if not match:
            return note
        base, octave = match.groups()
        return self.ENHARMONIC_MAP.get(base, base) + octave

    def strip_octave(self, note):
        return note.replace("'''", "").replace("''", "").replace("'", "")

    def build_fingering_map(self):
        for string, open_note in self.STARTING_NOTES.items():
            self._assign_open_string(string, open_note)
            self._assign_fingerings_for_string(string, open_note)

    def _assign_open_string(self, string, note):
        self.fingering_map[note] = {"string": string, "position": "I", "finger": "0"}
        self.other_fingering_map.append({"note": note, "string": string, "position": "I", "finger": "0"})

    def _assign_fingerings_for_string(self, string, open_note):
        try:
            start_idx = self.note_names.index(open_note) + 1
        except ValueError:
            return

        position_idx = 0
        finger = 1
        notes_assigned = 0
        fourth_finger_count = 0

        while start_idx < len(self.note_names) and notes_assigned < 27:
            note = self.note_names[start_idx]
            if note not in self.current_scale:
                start_idx += 1
                continue

            position = self.POSITIONS[position_idx]
            self.fingering_map[note] = {"string": string, "position": position, "finger": str(finger)}
            self.other_fingering_map.append({"note": note, "string": string, "position": position, "finger": str(finger)})

            if finger == 2 and string == "E" and position_idx == 0:
                position_idx = min(position_idx + 1, len(self.POSITIONS) - 1)
                finger = 1
            elif finger == 4:
                fourth_finger_count += 1
                if fourth_finger_count > 1:
                    break
            else:
                finger += 1



            start_idx += 1
            notes_assigned += 1

    def get_fingering_map(self):
        return self.fingering_map

    def get_unique_fingerings(self):
        return [dict(t) for t in {tuple(d.items()) for d in self.other_fingering_map}]

    def display_sample(self, count=20):
        print("🎻 Fingering Map (sample):")
        print(self.fingering_map)
        for note, info in list(self.fingering_map.items())[:count]:
            print(f"{note}: {info}")

violin_map = ViolinFingeringMap(tonic='g', scale_type='major', octaves=3)
violin_map.build_fingering_map()
violin_map.display_sample()

