# European note names (with octave markings)
note_names = [
    'c', 'cis', 'd', 'dis', 'e', 'f', 'fis', 'g', 'gis', 'a', 'ais', 'b',
    "c'", "cis'", "d'", "dis'", "e'", "f'", "fis'", "g'", "gis'", "a'", "ais'", "b'",
    "c''", "cis''", "d''", "dis''", "e''", "f''", "fis''", "g''", "gis''", "a''", "ais''", "b''",
    "c'''", "cis'''", "d'''", "dis'''", "e'''", "f'''"
]

# Starting notes for each string
starting_notes = {
    'G': 'g',
    'D': 'd',
    'A': "a'",
    'E': "e''"
}

# Violin positions
positions = ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X', 'XI', 'XII', 'XIII', 'XIV', 'XV']



# Define C major scale (can be replaced with any scale)

# Helper: remove octave marks
def strip_octave(note):
    return note.replace("'''", "").replace("''", "").replace("'", "")

# Check if note is in scale (natural or altered but diatonically valid)
def is_in_scale(note, scale):
    base = strip_octave(note)
    return base in scale

# Initialize fingering map
fingering_map_violin = {}
other_fingering_map_violin = []

def get_major_scale(tonic):
    major_steps = [0, 2, 4, 5, 7, 9, 11]
    chromatic = ['c', 'cis', 'd', 'dis', 'e', 'f', 'fis', 'g', 'gis', 'a', 'ais', 'b']
    start = chromatic.index(tonic)
    return {chromatic[(start + step) % 12] for step in major_steps}

# Set current scale context
current_scale = get_major_scale('d')  # D major
def generate_scale(tonic, scale_type='major', octaves=3):
    chromatic = ['c', 'cis', 'd', 'dis', 'e', 'f', 'fis', 'g', 'gis', 'a', 'ais', 'b']
    major_steps = [2, 2, 1, 2, 2, 2, 1]
    minor_steps = [2, 1, 2, 2, 1, 2, 2]
    steps = major_steps if scale_type == 'major' else minor_steps

    start_index = chromatic.index(tonic)
    scale_notes = []
    octave_marks = ["", "'", "''", "'''"]

    for octave in range(octaves):
        idx = start_index
        for step in [0] + steps:
            note = chromatic[idx % 12] + octave_marks[octave]
            scale_notes.append(note)
            idx += step

    return set(scale_notes)
my_current_scale = generate_scale('d','major',octaves=3)  # D major
print("current scale",my_current_scale)


# Loop through each string
for string in ['G', 'D', 'A', 'E']:
    print(string)
    note_index = note_names.index(starting_notes[string]) + 1
    position_index = 0
    position = positions[position_index]
    finger = '1'
    firstnotepassee=False
    notes_assigned = 0
    other_fingering_map_violin.append({
        "note": starting_notes[string],
        "string": string,
        "position": "I",
        "finger": "0"
    })

    while note_index < len(note_names) and notes_assigned < 27:
        # Block of 8 notes
        block = note_names[note_index:note_index + 8]
        mynumber=0

        for note in block:
            mynumber+=1
            if notes_assigned >= 27 or note_index >= len(note_names):
                break
        
            # Assign fingering
            other_fingering_map_violin.append({
                "note": note,
                "string": string,
                "position": position,
                "finger": finger
            })
            fingering_map_violin[note] = {
                "string": string,
                "position": position,
                "finger": finger
            }
        
            ## Increment finger if note is natural or in scale
            ##if not ('is' in note or 'es' in note) or note in my_current_scale:
            #if note in my_current_scale:
            if note_index + mynumber + 1 < len(note_names):
                next_note = note_names[mynumber + note_index + 1]
                if next_note in my_current_scale:
                    if finger == '1':
                        finger = '2'
                    elif finger == '2':
                        finger = '3'
                    elif finger == '3':
                        finger = '4'
                    elif finger == '4':
                        finger = '4'

        
        # ✅ Increment position if first note of blcok is in scale past first note

        if len(block) > 1 and block[1] in my_current_scale and firstnotepassee is True:
            print("next position", block[1])
            position_index += 1
            if position_index < len(positions):
                position = positions[position_index]
                print(position)

            #else:
            #    break
        finger = '1'
        if len(block) > 1 and block[1] in my_current_scale:
            firstnotepassee=True

        
        
        note_index += 1
        notes_assigned += 1

        ## After each block of 8, increment position
        #position_index += 1
        #if position_index < len(positions):
        #    position = positions[position_index]
        #    finger = '1'  # No open string after position I
        #else:
        #    break

# Display sample output
print("🎻 Fingering Map (sample):")
print(other_fingering_map_violin)
for note, info in list(fingering_map_violin.items())[:20]:
    print(f"{note}: {info}")

