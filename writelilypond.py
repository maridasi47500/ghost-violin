from flask import Flask, render_template, request
app = Flask(__name__)

def to_lilypond(note): 
     return note.replace("'''", "'''").replace("''", "''").replace("'", "'")
# Your fingering map here (import or define)
fingering_map_violin = [{'note': 'g', 'string': 'G', 'position': 'I', 'finger': '0'}, {'note': 'gis', 'string': 'G', 'position': 'I', 'finger': '1'}, {'note': 'a', 'string': 'G', 'position': 'I', 'finger': '1'}, {'note': 'ais', 'string': 'G', 'position': 'I', 'finger': '2'}, {'note': 'b', 'string': 'G', 'position': 'I', 'finger': '2'}, {'note': "c'", 'string': 'G', 'position': 'I', 'finger': '3'}, {'note': "cis'", 'string': 'G', 'position': 'I', 'finger': '4'}, {'note': "d'", 'string': 'G', 'position': 'I', 'finger': '4'}, {'note': "dis'", 'string': 'G', 'position': 'II', 'finger': '1'}, {'note': "e'", 'string': 'G', 'position': 'II', 'finger': '1'}, {'note': "f'", 'string': 'G', 'position': 'II', 'finger': '2'}, {'note': "fis'", 'string': 'G', 'position': 'II', 'finger': '3'}, {'note': "g'", 'string': 'G', 'position': 'II', 'finger': '4'}, {'note': "gis'", 'string': 'G', 'position': 'II', 'finger': '4'}, {'note': "a'", 'string': 'G', 'position': 'II', 'finger': '4'}, {'note': "ais'", 'string': 'G', 'position': 'II', 'finger': '4'}, {'note': "b'", 'string': 'G', 'position': 'III', 'finger': '1'}, {'note': "c''", 'string': 'G', 'position': 'III', 'finger': '2'}, {'note': "cis''", 'string': 'G', 'position': 'III', 'finger': '3'}, {'note': "d''", 'string': 'G', 'position': 'III', 'finger': '4'}, {'note': "dis''", 'string': 'G', 'position': 'III', 'finger': '4'}, {'note': "e''", 'string': 'G', 'position': 'III', 'finger': '4'}, {'note': "f''", 'string': 'G', 'position': 'III', 'finger': '4'}, {'note': "fis''", 'string': 'G', 'position': 'III', 'finger': '4'}, {'note': "g''", 'string': 'G', 'position': 'IV', 'finger': '1'}, {'note': "gis''", 'string': 'G', 'position': 'IV', 'finger': '2'}, {'note': "a''", 'string': 'G', 'position': 'IV', 'finger': '2'}, {'note': 'd', 'string': 'D', 'position': 'I', 'finger': '0'}, {'note': 'dis', 'string': 'D', 'position': 'I', 'finger': '1'}, {'note': 'e', 'string': 'D', 'position': 'I', 'finger': '1'}, {'note': 'f', 'string': 'D', 'position': 'I', 'finger': '2'}, {'note': 'fis', 'string': 'D', 'position': 'I', 'finger': '3'}, {'note': 'g', 'string': 'D', 'position': 'I', 'finger': '4'}, {'note': 'gis', 'string': 'D', 'position': 'I', 'finger': '4'}, {'note': 'a', 'string': 'D', 'position': 'I', 'finger': '4'}, {'note': 'ais', 'string': 'D', 'position': 'II', 'finger': '1'}, {'note': 'b', 'string': 'D', 'position': 'II', 'finger': '1'}, {'note': "c'", 'string': 'D', 'position': 'II', 'finger': '2'}, {'note': "cis'", 'string': 'D', 'position': 'II', 'finger': '3'}, {'note': "d'", 'string': 'D', 'position': 'II', 'finger': '4'}, {'note': "dis'", 'string': 'D', 'position': 'II', 'finger': '4'}, {'note': "e'", 'string': 'D', 'position': 'II', 'finger': '4'}, {'note': "f'", 'string': 'D', 'position': 'II', 'finger': '4'}, {'note': "fis'", 'string': 'D', 'position': 'III', 'finger': '1'}, {'note': "g'", 'string': 'D', 'position': 'III', 'finger': '2'}, {'note': "gis'", 'string': 'D', 'position': 'III', 'finger': '3'}, {'note': "a'", 'string': 'D', 'position': 'III', 'finger': '3'}, {'note': "ais'", 'string': 'D', 'position': 'III', 'finger': '4'}, {'note': "b'", 'string': 'D', 'position': 'III', 'finger': '4'}, {'note': "c''", 'string': 'D', 'position': 'III', 'finger': '4'}, {'note': "cis''", 'string': 'D', 'position': 'III', 'finger': '4'}, {'note': "d''", 'string': 'D', 'position': 'IV', 'finger': '1'}, {'note': "dis''", 'string': 'D', 'position': 'IV', 'finger': '2'}, {'note': "e''", 'string': 'D', 'position': 'IV', 'finger': '2'}, {'note': "a'", 'string': 'A', 'position': 'I', 'finger': '0'}, {'note': "ais'", 'string': 'A', 'position': 'I', 'finger': '1'}, {'note': "b'", 'string': 'A', 'position': 'I', 'finger': '1'}, {'note': "c''", 'string': 'A', 'position': 'I', 'finger': '2'}, {'note': "cis''", 'string': 'A', 'position': 'I', 'finger': '3'}, {'note': "d''", 'string': 'A', 'position': 'I', 'finger': '4'}, {'note': "dis''", 'string': 'A', 'position': 'I', 'finger': '4'}, {'note': "e''", 'string': 'A', 'position': 'I', 'finger': '4'}, {'note': "f''", 'string': 'A', 'position': 'II', 'finger': '1'}, {'note': "fis''", 'string': 'A', 'position': 'II', 'finger': '2'}, {'note': "g''", 'string': 'A', 'position': 'II', 'finger': '3'}, {'note': "gis''", 'string': 'A', 'position': 'II', 'finger': '4'}, {'note': "a''", 'string': 'A', 'position': 'II', 'finger': '4'}, {'note': "ais''", 'string': 'A', 'position': 'II', 'finger': '4'}, {'note': "b''", 'string': 'A', 'position': 'II', 'finger': '4'}, {'note': "c'''", 'string': 'A', 'position': 'II', 'finger': '4'}, {'note': "cis'''", 'string': 'A', 'position': 'III', 'finger': '1'}, {'note': "d'''", 'string': 'A', 'position': 'III', 'finger': '2'}, {'note': "dis'''", 'string': 'A', 'position': 'III', 'finger': '3'}, {'note': "e'''", 'string': 'A', 'position': 'III', 'finger': '3'}, {'note': "f'''", 'string': 'A', 'position': 'III', 'finger': '4'}, {'note': "e''", 'string': 'E', 'position': 'I', 'finger': '0'}, {'note': "f''", 'string': 'E', 'position': 'I', 'finger': '1'}, {'note': "fis''", 'string': 'E', 'position': 'I', 'finger': '2'}, {'note': "g''", 'string': 'E', 'position': 'I', 'finger': '3'}, {'note': "gis''", 'string': 'E', 'position': 'I', 'finger': '4'}, {'note': "a''", 'string': 'E', 'position': 'I', 'finger': '4'}, {'note': "ais''", 'string': 'E', 'position': 'I', 'finger': '4'}, {'note': "b''", 'string': 'E', 'position': 'I', 'finger': '4'}, {'note': "c'''", 'string': 'E', 'position': 'II', 'finger': '1'}, {'note': "cis'''", 'string': 'E', 'position': 'II', 'finger': '2'}, {'note': "d'''", 'string': 'E', 'position': 'II', 'finger': '3'}, {'note': "dis'''", 'string': 'E', 'position': 'II', 'finger': '4'}, {'note': "e'''", 'string': 'E', 'position': 'II', 'finger': '4'}, {'note': "f'''", 'string': 'E', 'position': 'II', 'finger': '4'}]


@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        string = request.form['string']
        position = request.form['position']
        finger = request.form['finger']
        alteration = request.form['alteration']  # 'diese' or 'bemol'

        # Find matching note
        for data in fingering_map_violin:
            if data['string'] == string and data['position'] == position and data['finger'] == finger:
                base_note = data['note']
                break
        else:
            base_note = None

        # Apply alteration
        if base_note:
            if alteration == 'diese' and not 'is' in base_note:
                base_note = base_note.replace('es', '') + 'is'
            elif alteration == 'bemol' and not 'es' in base_note:
                base_note = base_note.replace('is', '') + 'es'

            # Convert to LilyPond format
            lilypond_note = base_note.replace("'''", "'''").replace("''", "''").replace("'", "'")
            result = f"LilyPond note: {lilypond_note}"

    return render_template('form.html', result=result)

