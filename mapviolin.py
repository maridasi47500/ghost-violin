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

def get_major_scale(tonic):
    major_steps = [0, 2, 4, 5, 7, 9, 11]
    chromatic = ['c', 'cis', 'd', 'dis', 'e', 'f', 'fis', 'g', 'gis', 'a', 'ais', 'b']
    start = chromatic.index(tonic)
    return {chromatic[(start + step) % 12] for step in major_steps}

# Set current scale context
current_scale = get_major_scale('d')  # D major

# Loop through each string
for string in ['G', 'D', 'A', 'E']:
    note_index = note_names.index(starting_notes[string])
    position_index = 0
    position = positions[position_index]
    finger = '0' if position == 'I' else '1'
    notes_assigned = 0

    while note_index < len(note_names) and notes_assigned < 27:
        # Block of 8 notes
        block = note_names[note_index:note_index + 8]

        for note in block:
            if notes_assigned >= 27 or note_index >= len(note_names):
                break

            # Assign fingering
            fingering_map_violin[note] = {
                "string": string,
                "position": position,
                "finger": finger
            }

            # Increment finger only if note is natural or belongs to scale
            if not ('is' in note or 'es' in note) or is_in_scale(note, current_scale):
                if finger == '0':
                    finger = '1'
                elif finger == '1':
                    finger = '2'
                elif finger == '2':
                    finger = '3'
                elif finger == '3':
                    finger = '4'
                elif finger == '4':
                    finger = '4'  # Stay at 4

            note_index += 1
            notes_assigned += 1

        # After each block of 8, increment position
        position_index += 1
        if position_index < len(positions):
            position = positions[position_index]
            finger = '1'  # No open string after position I
        else:
            break

# Display sample output
print("🎻 Fingering Map (sample):")
for note, info in list(fingering_map_violin.items())[:20]:
    print(f"{note}: {info}")

