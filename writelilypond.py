from flask import Flask, render_template, request
from mapviolin import ViolinFingeringMap
app = Flask(__name__)

def to_lilypond(note): 
     return note.replace("'''", "'''").replace("''", "''").replace("'", "'")
# Your fingering map here (import or define)
violin_map = ViolinFingeringMap(tonic='g', scale_type='major', octaves=3)
violin_map.build_fingering_map()
fingering_map_violin = violin_map.get_unique_fingerings()


print(fingering_map_violin)






@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
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
        for base_note in base_notes:
            number+=1
            #if alteration == 'diese' and not 'is' in base_note:
            #    base_note = base_note.replace('es', '') + 'is'
            #elif alteration == 'bemol' and not 'es' in base_note:
            #    base_note = base_note.replace('is', '') + 'es'

            ## Convert to LilyPond format
            #lilypond_note = base_note.replace("'''", "'''").replace("''", "''").replace("'", "'")
            result += f"LilyPond note n°{number}: {base_note}<br>"

    return render_template('form.html', result=result,tonalite=violin_map.get_my_scale_name())

if __name__ == '__main__':
    app.run()
