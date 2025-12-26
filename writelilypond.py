from flask import Flask, render_template, request
from mapviolin import ViolinFingeringMap
from galaxymusic import ViolinFingeringMapMusic
#from violinmaprefactored import ViolinFingeringMap
import subprocess
from subprocess import run

app = Flask(__name__)

def to_lilypond(note): 
     return note.replace("'''", "'''").replace("''", "''").replace("'", "'")
# Your fingering map here (import or define)
violin_map = ViolinFingeringMap(tonic='g', scale_type='major', octaves=3)
violin_map.build_fingering_map()
violin_map.save_my_fingering_in_html()
violin_map_music = ViolinFingeringMapMusic(tonic='g', scale_type='major', octaves=3)
violin_map_music.build_fingering_map()
violin_map_music.save_my_scales_in_one_position_in_html()
fingering_map_violin = violin_map.get_unique_fingerings()


print(fingering_map_violin)





@app.route('/mynote', methods=['GET'])
def mynote():
    result = None
    return render_template('myscore/myscore.html')

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    myscorenotesone=""
    string = ""
    position = ""
    finger = ""
    if request.method == 'POST':
        string = request.form['string']
        position = request.form['position']
        finger = request.form['finger']
        alteration = request.form['alteration']  # 'diese' or 'bemol'
        base_notes=[]
        # Find matching note
        for data in fingering_map_violin:
            if data['string'] == string and data['position'] == position and data['finger'] == finger:
                base_notes.append(data['note'])
        else:
            base_note = None

        # Apply alteration
        result="sur la string de "+string+ " en "+position+"e position avec le "+finger+"e doigt, je pourrais faire les notes:"
        number=1
        myscorenotes=""


        for base_note in base_notes:
            number+=1
            #if alteration == 'diese' and not 'is' in base_note:
            #    base_note = base_note.replace('es', '') + 'is'
            #elif alteration == 'bemol' and not 'es' in base_note:
            #    base_note = base_note.replace('is', '') + 'es'

            ## Convert to LilyPond format
            #lilypond_note = base_note.replace("'''", "'''").replace("''", "''").replace("'", "'")
            result += f"LilyPond note n°{number}: {base_note}<br>"
            #myscorenotes += " "+base_note
            myscorenotesone += base_note.replace("'","o")
            #myscorenotes += "\\relative c {\n"+base_note+"}\n"
            myscorenotes += " "+base_note
        with open("./scores/myscore"+myscorenotesone+".html", "w") as f:
         #f.write("<lilypond fragment staffsize=54>\\version \"2.24.3\"\n\n"+myscorenotes+"\n\n</lilypond>")
         f.write("<lilypond fragment staffsize=54>\\version \"2.24.3\"\n\\absolute {\n"+myscorenotes+"\n}\n</lilypond>")

        with open("demofile.sh", "w") as f:
         f.write("(cd scores/ && lilypond-book myscore"+myscorenotesone+".html -f html --output myscore"+myscorenotesone+")")
        rc = subprocess.Popen(["sh", "./demofile.sh"])

    return render_template('form.html', result=result,tonalite=violin_map.get_my_scale_name(), myscorenotes=myscorenotesone, string=string, position=position, finger=finger)

if __name__ == '__main__':
    app.run()
