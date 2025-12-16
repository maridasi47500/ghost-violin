import re

        #'c', 'cis', 'd', 'dis', 'e', 'f', 'fis', 'g', 'gis', 'a', 'ais', 'b',
class ViolinFingeringMap:
    note_names = [
        'g', 'gis', 'a', 'ais', 'b',

        "c'", "cis'", "d'", "dis'", "e'", "f'", "fis'", "g'", "gis'", "a'", "ais'", "b'",
        "c''", "cis''", "d''", "dis''", "e''", "f''", "fis''", "g''", "gis''", "a''", "ais''", "b''",
        "c'''", "cis'''", "d'''", "dis'''", "e'''", "f'''"
    ]

    enharmonic_map = {
        "ces": "b", "des": "cis", "ees": "dis", "fes": "e", "ges": "fis", "aes": "gis", "bes": "ais",
        "cis": "des", "dis": "ees", "eis": "f", "fis": "ges", "gis": "aes", "ais": "bes", "bis": "c"
    }

    starting_notes = {
        'G': 'g',
        'D': "d'",
        'A': "a'",
        'E': "e''"
    }

    positions = ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X', 'XI', 'XII', 'XIII', 'XIV', 'XV']

    def __init__(self, tonic='g', scale_type='major', octaves=3):
        self.tonic = tonic
        self.scale_type = scale_type
        self.octaves = octaves
        self.fingering_map = {}
        self.other_fingering_map = []
        self.current_scale = self.generate_scale(tonic, scale_type, octaves)
    def get_my_scale_name(self):
        return self.tonic+" "+self.scale_type

    def normalize(self, note):
        match = re.match(r"([a-g][ei]s|[a-g]es|[a-g])([',]*)$", note)
        if not match:
            return note
        base, octave = match.groups()
        return self.enharmonic_map.get(base, base) + octave

    def strip_octave(self, note):
        return note.replace("'''", "").replace("''", "").replace("'", "")

    def generate_scale(self, tonic, scale_type='major', octaves=3):
        chromatic = ['c', 'cis', 'd', 'dis', 'e', 'f', 'fis', 'g', 'gis', 'a', 'ais', 'b']
        chromatic2 = ['c', 'cis', 'd', 'dis', 'e', 'f', 'fis', 'g', 'gis', 'a', 'ais', 'b']
        chromatic1 = ['c', 'des', 'd', 'ees', 'e', 'f', 'ges', 'g', 'aes', 'a', 'bes', 'b']

        steps = [2, 2, 1, 2, 2, 2, 1] if scale_type == 'major' else [2, 1, 2, 2, 1, 2, 2]
        try:
            start_index = chromatic.index(tonic) #g string, 
        except:
            chromatic = ['c', 'des', 'd', 'ees', 'e', 'f', 'ges', 'g', 'aes', 'a', 'bes', 'b']
            start_index = chromatic.index(tonic)
        scale_notes = []
        octave_marks = ["", "'", "''", "'''", "''''"]
        #de la g string a vide a la premiere note
        #increment octave marks au "g" 
        #mapviolin for lilypod

        myoctavemark=0
        for octave in range(octaves+1):
            idx = start_index
            for step in [0] + steps:
                
                note = chromatic[idx % 12] + octave_marks[myoctavemark]
                scale_notes.append(note)
                if chromatic[idx % 12] == "b":
                    myoctavemark+=1
                
                idx += step

        return set(scale_notes)

    def build_fingering_map(self):
        for string in ['G', 'D', 'A', 'E']:
            print("string",string)
            note_index = self.note_names.index(self.starting_notes[string]) + 1
            position_index = 0
            position = self.positions[position_index]
            finger = '1'
            firstnotepassee = False
            notes_assigned = 0
            if string == "G":
                mynote=string.lower()
            elif string == "D" or string == "A":
                mynote=string.lower()+"'"
            elif string == "E":
                mynote=string.lower()+"''"
            self.fingering_map[mynote] = {
                "string": string,
                "position": "I",
                "finger": "0"
            }

            self.other_fingering_map.append({
                "note": self.starting_notes[string],
                "string": string,
                "position": "I",
                "finger": "0"
            })

            while note_index < len(self.note_names) and notes_assigned < 27:
                block = self.note_names[note_index:note_index + 8]
                mynumber = 0

                for note in block:
                    print(note,"note")

                    if notes_assigned >= 27 or note_index >= len(self.note_names):
                        break

                    self.other_fingering_map.append({
                        "note": note,
                        "string": string,
                        "position": position,
                        "finger": finger
                    })

                    self.fingering_map[note] = {
                        "string": string,
                        "position": position,
                        "finger": finger
                    }
                    print(string, finger)

                    if note_index + mynumber + 1 < len(self.note_names):
                        next_note = self.note_names[note_index + mynumber + 1]
                        prev_note = self.note_names[note_index + mynumber - 1] if mynumber > 1 else None
                        
                    
                        if next_note in self.current_scale:
                            print("prochaine ntoe dans la gamme")

                            if position == "I" and finger == 1 and note not in self.current_scale:
                                print("NE FAIS RIEN")



                            else:
                                finger = str(min(int(finger) + 1, 4))
                    mynumber += 1


                if len(block) > 1 and block[1] in self.current_scale:
                    print("prochaine note, et deuxieme note du bloque dans la gamme")
                    if position == "I" and note_index < self.note_names.index(self.starting_notes[string]) + 2 and (block[0] not in self.current_scale):
                        print("do nothgiun")
                    else:
                        position_index += 1
                    
                    if position_index < len(self.positions):
                        position = self.positions[position_index]
                        print("position", position)
                    finger = '1'
                    firstnotepassee = True

                note_index += 1
                notes_assigned += 1

    def get_the_fingering_map(self):
        return self.fingering_map
    def get_unique_fingerings(self):
        return [dict(t) for t in {tuple(d.items()) for d in self.other_fingering_map}]

    def display_sample(self, count=20):
        print("🎻 Fingering Map (sample):")
        #print(list(self.get_unique_fingerings()))
        print(self.get_the_fingering_map())
        #for note in list(self.get_unique_fingerings())[:count]:
        #    print(f"{note["string"]}: {note["position"]}, {note["finger"]}: {note["note"]}")

violin_map = ViolinFingeringMap(tonic='bes', scale_type='major', octaves=3)
violin_map.build_fingering_map()
violin_map.display_sample()

