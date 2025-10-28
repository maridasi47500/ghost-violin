import re

class ViolinFingeringMap:
    chromatic = ['c', 'cis', 'd', 'ees', 'e', 'f', 'fis', 'g', 'ais', 'a', 'bes', 'b']
    octave_marks = ["", "'", "''", "'''","''''","'''''","''''''"]
    note_names = [
        'g', 'gis', 'a', 'ais', 'b', 
        'c', 'cis', 'd', 'dis', 'e', 'f', 'fis', 'g', 'gis', 'a', 'ais', 'b',
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
        octave=0
        idx=self.chromatic.index("g")
        scale_notes=[]
        for numberoctave in range(octaves):
            for numbernote in range(len(self.chromatic)):
                print(octave,idx)
                if "c" in self.chromatic[idx % 12] and "cis" not in self.chromatic[idx % 12]:
                    octave += 1
                note = self.chromatic[idx % 12] + self.octave_marks[octave]


                #if "g" in note:
                #    break
                scale_notes.append(note)

                print(scale_notes)
                idx += 1
        self.note_names=scale_notes
        print(scale_notes)
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
        chromatic = ['c', 'cis', 'd', 'ees', 'e', 'f', 'fis', 'g', 'ais', 'a', 'bes', 'b']
        violinfirst="g"

        steps = [2, 2, 1, 2, 2, 2, 1] if scale_type == 'major' else [2, 1, 2, 2, 1, 2, 2]
        violin_start = chromatic.index(violinfirst) #g string, 
        try:
            start_index = chromatic.index(tonic) #g string, 
        except:
            chromatic = ['c', 'des', 'd', 'dis', 'e', 'f', 'ges', 'g', 'gis', 'a', 'ais', 'b']
            start_index = chromatic.index(tonic)
        scale_notes = []
        octave_marks = ["", "'", "''", "'''"]
        #de la g string a vide a la premiere note
        #increment octave marks au "g" 
        #mapviolin for lilypod

        #for octave in range(octaves):
        #    idx = start_index
        #    for step in [0] + steps:
        #        note = chromatic[idx % 12] + octave_marks[octave]
        #        scale_notes.append(note)
        #        idx += step

        octave=0
        idx = start_index
        myid = start_index
        paspremier=False
        if violin_start != myid:

            for step in  list(reversed(list(steps))):
                print(scale_notes)
                note = chromatic[myid % 12]
                if chromatic.index("g") > chromatic.index(note):
                    break
                if paspremier is not False:
                    scale_notes.insert(0,note)
                myid -= step

                if myid > len(chromatic):
                    myid=0
                paspremier=True

        #for octave in range(octaves):
        #for step in [0] + steps:
        for numberoctave in range(octaves):
            for step in steps:


                if "c" in chromatic[idx % 12] and "cis" not in chromatic[idx % 12]:
                    octave += 1
                note = chromatic[idx % 12] + octave_marks[octave]

                scale_notes.append(note)

                print(scale_notes)
                idx += step
        print(scale_notes)


        return set(scale_notes)

    def build_fingering_map(self):
        for string in ['G', 'D', 'A', 'E']:
            print("string",string)
            try:
                note_index = self.note_names.index(self.starting_notes[string]) + 1
            except:
                note_index = self.note_names.index(self.starting_notes[string]) + 1
            position_index = 0
            position = self.positions[position_index]
            finger = '1'
            firstnotepassee = False
            notes_assigned = 0
            if string == "G":
                mynote=string.lower()
            if string == "D" or string == "A":
                mynote=string.lower()+"'"
            elif string == "E":
                mynote=string.lower()+"''"
            self.fingering_map[mynote] = {
                "string": string,
                "position": "I",
                "finger": "0"
            }
            fourthfinger=0

            self.other_fingering_map.append({
                "note": self.starting_notes[string],
                "string": string,
                "position": "I",
                "finger": "0"
            })



            newblock=0
            mynumber=0
            while note_index < len(self.note_names) and notes_assigned < 27:
                #if fourthfinger > 1 and mynumber >= 8 and newblock>7:
                #   break

                block = self.note_names[note_index:note_index + 8]
                newblock+=1

                mynumber = 0


                if notes_assigned >= 27 or note_index >= len(self.note_names):
                    break

                for note in block:
                    print(newblock,mynumber,fourthfinger)
                    if finger=="4" and mynumber == 0:
                        break
                    #print(note,"note")
                    print(mynumber)



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
                    #print(string, finger, note,fourthfinger)
                    if finger=="4" and position == "III":
                       print("ERTYUIKJHVFYUI")
                       print(string, finger, note,fourthfinger)
                    if finger=="4":
                       fourthfinger+=1
                    if fourthfinger > 1:
                       break


                    if note_index + mynumber + 1 < len(self.note_names):
                        next_note = self.note_names[note_index + mynumber + 1]
                        prev_note = self.note_names[note_index + mynumber - 1] if mynumber > 1 else None
                        
                    
                        if next_note in self.current_scale:
                            #print("prochaine ntoe dans la gamme")

                            if position == "I" and finger == 1 and note not in self.current_scale:
                                print("NE FAIS RIEN")



                            else:
                                finger = str(min(int(finger) + 1, 4))
                    mynumber += 1


                if len(block) > 1 and block[1] in self.current_scale:
                    #print("prochaine note, et deuxieme note du bloque dans la gamme")
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

