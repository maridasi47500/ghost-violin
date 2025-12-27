import re
import subprocess
from mapviolin import ViolinFingeringMap

from subprocess import run


        #'c', 'cis', 'd', 'dis', 'e', 'f', 'fis', 'g', 'gis', 'a', 'ais', 'b',
class ViolinFingeringMapMusic:
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

    def __init__(self, tonic='g', scale_type='major', octaves=6):
        self.tonic = tonic
        self.scale_type = scale_type
        self.octaves = octaves
        self.fingering_map = {}
        self.other_fingering_map = []
        self.current_scale = self.generate_scale(tonic, scale_type, octaves)
        self.current_scale_with_enharmonic = self.generate_scale(tonic, scale_type, octaves)
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
    def scales_in_one_position(self, positions = 15):
        myscale=self.current_scale
        try:
            idx=self.current_scale.index("a") #premiere note colonne
        except:
            try:
                idx=self.current_scale.index("ais")
            except:
                idx=self.current_scale.index("aes")
        idy=idx #premiere note ligne
        notes=[]
        notes.append(myscale[idx]+"4")

        paspremier=False
        for x in range(positions):

            idy=idx
          
            nombre=16 if paspremier else 15
            nombre2=15 if paspremier else 15
            for y in range(nombre):
                idy+=1
                notes.append(myscale[idy])
            notes.append(myscale[idy - 1])
            for y in range(nombre2):

                notes.append(myscale[idy])
                idy-=1
            #notes.append("\\break")
            if paspremier is True:
                idx+=1
            paspremier=True
        return notes
    def save_my_scales_in_one_position_in_html(self, count=20):
        #print("🎻 Fingering Map (sample):")
        #print(list(self.get_unique_fingerings()))
        octaves=5
        myscore=""
        for tonic in ["a","b","c","e","f","g"]:
            for scale_type in ["major", "minor"]:
                violin_map = ViolinFingeringMap(tonic=tonic, scale_type=scale_type, octaves=octaves, open_string=False)
                violin_map.build_fingering_map()
                violin_map.get_my_scale_enharmonic_scale()


                self.current_scale = self.generate_scale(tonic, scale_type, octaves)
                myscore+="<h1>Scales in One position on the violin for "+str(tonic)+" "+scale_type+" scale</h1><lilypond fragment staffsize=32>\\key "+tonic+" \\"+scale_type+"\n"
                mystring=""
                prevstring=""
                myposition=0
                nbnotes=0
                for y in self.scales_in_one_position():
                    if y == "\\break":
                        myscore+=" "  +y+("_\""+self.positions[myposition]+"\"" if nbnotes == 1 else "")
                    else:
                        nbnotes+=1
                        try:

                            try:
                                x=violin_map.search_for_note(y.replace("4",""), myposition)
                                if len(x) == 0:
                                    manote=self.enharmonic_map[y.replace("4","").replace("'","")]+y.replace(y.replace("4","").replace("'",""), "")
                                    x=violin_map.search_for_note(manote, myposition)
                            except:
                                #print("erreur edtgfeqrh note;", y)
                                #print("erreur edtgfeqrh positions", self.positions[myposition])
                                print("")
                                #manote=self.enharmonic_map[y.replace("4","").replace("'","")]+y.replace(y.replace("4","").replace("'",""), "")
                                #x=violin_map.search_for_note(manote, myposition)
                            #print(x)
                            x=x[-1]
                            #print(x, y, self.positions[myposition])

                            mystring=x["string"]
                            myscore+=" "  +x["note"]+"^"+str(x["finger"])+("_\""+x["position"]+"\"" if nbnotes == 1 else "")+("_\""+x["string"]+"\"" if mystring != prevstring else "")
                            prevstring=x["string"]
                        except:
                            #print(y, self.positions[myposition])
                            myscore+=" "  +y+("_\""+self.positions[myposition]+"\"" if nbnotes == 1 else "")

                        if nbnotes == 32:
                            myposition+=1
                            nbnotes=0
                    
                myscore+="</lilypond>"
        with open("mapviolinscales.html", "w") as f:
         f.write(myscore)
        with open("writescaleviolin.sh", "w") as f:
         f.write("(lilypond-book mapviolinscales.html -f html --output mesgammes)")
        rc = subprocess.Popen(["sh", "./writescaleviolin.sh"])


        

    def generate_scale(self, tonic, scale_type='major', octaves=3, with_enharmonic=False):
        chromatic = ['c', 'cis', 'd', 'dis', 'e', 'f', 'fis', 'g', 'gis', 'a', 'ais', 'b']
        chromatic2 = ['c', 'cis', 'd', 'dis', 'e', 'f', 'fis', 'g', 'gis', 'a', 'ais', 'b']
        chromatic1 = ['c', 'des', 'd', 'ees', 'e', 'f', 'ges', 'g', 'aes', 'a', 'bes', 'b']

        #steps = [0, 2, 2, 1, 2, 2, 2, 1] if scale_type == 'major' else [0, 2, 1, 2, 2, 1, 3, 1]
        steps = [2, 2, 1, 2, 2, 2, 1] if scale_type == 'major' else [2, 1, 2, 2, 1, 3, 1]
        try:
            start_index = chromatic.index(tonic) #g string, 
        except:
            chromatic = ['c', 'des', 'd', 'ees', 'e', 'f', 'ges', 'g', 'aes', 'a', 'bes', 'b']
            start_index = chromatic.index(tonic)
        scale_notes = []
        octave_marks = ["", "'", "''", "'''", "''''", "'''''", "''''''"]
        #de la g string a vide a la premiere note
        #increment octave marks au "g" 
        #mapviolin for lilypod
        mychromatic=[]
        nomnotes=["a","b","c","d","e","f","g"]
        start_index_nomnotes=nomnotes.index(tonic.replace("is","").replace("es",""))
        
        
        for octave in range(octaves+1):
            myoctavemark=octave
            idx = start_index
            idy = start_index_nomnotes
            #for step in [0] + steps:
            for step in steps:
                
        
                nameofnote=chromatic[idx % 12]
                simplenameofnote=nomnotes[idy % 7]
                #print(simplenameofnote+" in "+nameofnote)
                if simplenameofnote in nameofnote and step > 0:
                    note = chromatic[idx % 12] + octave_marks[myoctavemark]
                else:
                    try:
                        if step > 0:
                            note = self.enharmonic_map[chromatic[idx % 12]]+ octave_marks[myoctavemark]
                        else:
                            note = chromatic[idx % 12] + octave_marks[myoctavemark]
                    except:
                        #print("enharmonic error")
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
                        xxxxx="blabla"
                if "b" in chromatic[idx % 12]:
                    #print("B ENHARMONIC")
                    myoctavemark+=1
                
                idx += step
                if step > 0:
                    idy += 1
        
        #print(scale_notes)
        if "b" in tonic:
            scale_notes.insert(0, scale_notes[6].replace("'",""))
        return (scale_notes)

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
                block = self.note_names[note_index:note_index + 5]
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

                    if notes_assigned >= 27 or note_index >= len(self.note_names):
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
                        xxx="blabla"


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
                        xxxxx="blabla"
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
        print(self.get_the_fingering_map())
        #for note in list(self.get_unique_fingerings())[:count]:
        #    print(f"{note["string"]}: {note["position"]}, {note["finger"]}: {note["note"]}")
    def save_my_fingering_in_html(self, count=20):
        print("🎻 Fingering Map (sample):")
        #print(list(self.get_unique_fingerings()))
        myscore="<h1>all my fingering on all strings of the violin "+str(self.tonic)+" "+self.scale_type+" scale</h1><lilypond fragment staffsize=32>"
        myscorenotes="<p>"
        for x in self.current_scale_with_enharmonic:
            myscorenotes+=" "  +x
        myscorenotes+="-- "
        for x in self.other_fingering_map:
            myscore+=" "  +x["note"]+"^"+str(x["finger"])+"_\""+x["position"]+"\"_\""+x["string"]+"\"_\""+x["note"]+"\"_\""+("hey" if x["note"]  in self.current_scale_with_enharmonic else "")+"\""
            if x["note"] in self.current_scale_with_enharmonic:
                #print(self.current_scale_with_enharmonic)
                #
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

 

violin_map = ViolinFingeringMapMusic(tonic='g', scale_type='major', octaves=4)
violin_map.build_fingering_map()

violin_map.save_my_scales_in_one_position_in_html()
print(violin_map.scales_in_one_position())

