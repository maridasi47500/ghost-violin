import re
import subprocess
from subprocess import run


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

    def __init__(self, tonic='g', scale_type='major', octaves=5, open_string = True):
        self.tonic = tonic
        self.open_string = open_string
        self.scale_type = scale_type
        self.octaves = octaves
        self.fingering_map = {}
        self.other_fingering_map = []



        notes=["c", "cis", "d", "dis", "e", "f", "fis", "g", "gis", "a", "ais", "b"]
        idx=notes.index("g")
        octave_marks=["", "'","''","'''","''''","'''''","''''''"]
        octave_markid=0
        mynote=""

        for octaveid in range(self.octaves * len(notes)):
            noteid=notes[idx % len(notes)]
            mynote=noteid+octave_marks[octave_markid]
            if mynote not in self.note_names:
                self.note_names.append(mynote)
            if "b" in noteid:
                octave_markid+=1
            idx+=1
        print(self.note_names)
        self.current_scale = self.generate_scale(tonic, scale_type, octaves)
        self.current_scale_with_enharmonic = self.generate_scale(tonic, scale_type, octaves, with_enharmonic=True)
    def get_my_scale_enharmonic_scale(self):
        self.current_scale = self.generate_scale(self.tonic, self.scale_type, self.octaves, with_enharmonic=True)
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

    def generate_scale(self, tonic, scale_type='major', octaves=3, with_enharmonic=False):
        chromatic = ['c', 'cis', 'd', 'dis', 'e', 'f', 'fis', 'g', 'gis', 'a', 'ais', 'b']
        chromatic2 = ['c', 'cis', 'd', 'dis', 'e', 'f', 'fis', 'g', 'gis', 'a', 'ais', 'b']
        chromatic1 = ['c', 'des', 'd', 'ees', 'e', 'f', 'ges', 'g', 'aes', 'a', 'bes', 'b']

        steps = [0, 2, 2, 1, 2, 2, 2, 1] if scale_type == 'major' else [0, 2, 1, 2, 2, 1, 2, 2]
        try:
            start_index = chromatic.index(tonic) #g string, 
        except:
            chromatic = ['c', 'des', 'd', 'ees', 'e', 'f', 'ges', 'g', 'aes', 'a', 'bes', 'b']
            start_index = chromatic.index(tonic)
        scale_notes = []
        octave_marks = ["", "'", "''", "'''", "''''", "'''''", "''''''", "'''''''"]
        #de la g string a vide a la premiere note
        #increment octave marks au "g" 
        #mapviolin for lilypod


        for octave in range(octaves+1):
            myoctavemark=octave
            idx = start_index
            for step in [0] + steps:
                

                #print(myoctavemark)
                note = chromatic[idx % 12] + octave_marks[myoctavemark]
                scale_notes.append(note)
                if with_enharmonic is True:
                    #print("TRUE ENHARMONIC")
                    #print(chromatic[idx % 12])
                    try:
                        mynote = chromatic[idx % 12]
                        myenharmonic = self.enharmonic_map[mynote]+ octave_marks[myoctavemark]
                        scale_notes.append(myenharmonic)
                    except:
                        #print("enharmonic error")
                        xxururf="lkhj"
                if chromatic[idx % 12] == "b" and step > 0:
                    #print("B ENHARMONIC")
                    myoctavemark+=1
                
                idx += step

        print(scale_notes)
        return set(scale_notes)

    def build_fingering_map(self):
        for string in ['G', 'D', 'A', 'E']:
            #print("string",string)
            note_index = self.note_names.index(self.starting_notes[string]) + 1
            position_index = 0
            position = self.positions[position_index]
            finger = 1
            firstnotepassee = False
            notes_assigned = 0
            if string == "G":
                mynote=string.lower()
            elif string == "D" or string == "A":
                mynote=string.lower()+"'"
            elif string == "E":
                mynote=string.lower()+"''"
            if self.open_string is True or string == "G":
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

            
            premierpasse=False 
            while note_index < len(self.note_names) and notes_assigned < 27:
                block = self.note_names[note_index:note_index + 6]
                mynumber = 0

                if len(block) > 1 and block[0] in self.current_scale_with_enharmonic and notes_assigned > 1:
                    #print("premiere note du bloque dans la gamme")
                    position_index += 1
                    if position_index < len(self.positions):
                         position = self.positions[position_index]


                for note in block:
                    if mynumber == 0:
                        finger=1
                    #print(note,"note")

                    if notes_assigned >= 30 or note_index >= len(self.note_names):
                        break

                    self.other_fingering_map.append({
                        "note": note,
                        "string": string,
                        "position": position,
                        "finger": finger
                    })

                    try:
                        manote=self.enharmonic_map[note.replace("'","")]+note.replace(note.replace("'",""), "")
                        self.other_fingering_map.append({
                            "note": manote,
                            "string": string,
                            "position": position,
                            "finger": finger
                        })
                    except:
                        #print("enharmonic error (array)")
                        kjuhiu="ouh"


                    self.fingering_map[note] = {
                        "string": string,
                        "position": position,
                        "finger": finger
                    }
                    try:
                        manote=self.enharmonic_map[note.replace("'","")]+note.replace(note.replace("'",""), "")
                        self.fingering_map[manote] = {
                            "string": string,
                            "position": position,
                            "finger": finger
                        }
                    except:
                        #print("enharmonic error hash")
                        lkjho="lkhj"
                    #print(string, finger)

                    if note_index + mynumber + 1 < len(self.note_names):
                        next_note = self.note_names[note_index + mynumber + 1]
                        prev_note = self.note_names[note_index + mynumber - 1] if mynumber > 1 else None
                        
                    
                        if next_note in self.current_scale_with_enharmonic:
                            #print("prochaine ntoe dans la gamme")
                            finger = str(min(int(finger) + 1, 4))

                            #if position == "I" and finger == 1 and note not in self.current_scale_with_enharmonic:
                            #    print("NE FAIS RIEN")



                            #else:
                            #    finger = str(min(int(finger) + 1, 4))
                    mynumber += 1

                premierpasse =True




                    #if position == "I" and note_index < self.note_names.index(self.starting_notes[string]) + 2 and (block[0] not in self.current_scale_with_enharmonic):
                    #    print("do nothgiun")
                    #else:
                    #    position_index += 1
                    #    finger = 1
                    #
                    #if position_index < len(self.positions):
                    #    position = self.positions[position_index]
                    #    finger = 1
                    #    print("position", position)

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
        print(self.other_fingering_map)
        print(self.get_the_fingering_map())
        #for note in list(self.get_unique_fingerings())[:count]:
        #    print(f"{note["string"]}: {note["position"]}, {note["finger"]}: {note["note"]}")
    def save_my_fingering_in_html(self, count=20):
        print("🎻 Fingering Map (sample):")
        #print(list(self.get_unique_fingerings()))
        myscore="<h1>all my fingering on all strings of the violin "+str(self.tonic)+" "+self.scale_type+" scale</h1><lilypond fragment staffsize=32>\\key "+self.tonic+" \\"+self.scale_type+"\n"
        myscorenotes="<p>"
        for x in self.current_scale_with_enharmonic:
            myscorenotes+=" "  +x
        myscorenotes+="-- "
        for x in self.other_fingering_map:
            #myscore+=" "  +x["note"]+"^"+str(x["finger"])+"_\""+x["position"]+"\"_\""+x["string"]+"\"_\""+x["note"]+"\"_\""+("hey" if x["note"]  in self.current_scale_with_enharmonic else "")+"\""
            myscore+=" "  +x["note"]+"^"+str(x["finger"])+"_\""+x["position"]+"\"_\""+x["string"]+"\""
            if x["note"] in self.current_scale_with_enharmonic:
                #print(self.current_scale_with_enharmonic)
                
                #print(x["note"])
                myscorenotes+=" "  +x["note"]
        myscore+="</lilypond>"
        myscorenotes+="</p>"
        myscore+=myscorenotes
        with open("mapviolin.html", "w") as f:
         f.write(myscore)
        with open("writescale.sh", "w") as f:
         f.write("(lilypond-book mapviolin.html -f html --output gammes)")
        rc = subprocess.Popen(["sh", "./writescale.sh"])
    def right_note(self, w, note, pos):
        return w["note"] == note and w["position"] == self.positions[pos]
    
    def search_for_note(self, note, pos): 
        li = self.other_fingering_map
        res = filter(lambda x: self.right_note(x, note, pos), li)
        return (list(res))


 

violin_map = ViolinFingeringMap(tonic='a', scale_type='major', octaves=6)
violin_map.build_fingering_map()
#violin_map.save_my_fingering_in_html()
violin_map.display_sample()

