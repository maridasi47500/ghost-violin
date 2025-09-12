import re
import os
with open("pavanehey.ly", "r", encoding="utf-8") as file:
    original_score = file.read()




# Function to insert bowing marks
def insert_bowing(score):
    slur_pattern = r"(\\slurUp\s*\()([^\)]+)"
    bowings = ["^\\upbow", "^\\downbow"]
    bow_index = 1
    if bow_index == 1:
        bow_index = 0
    else:
        bow_index = 1
    

    def add_bow(match):


        notes = match.group(2).strip()
        # Find first note and insert bowing
        note_match = re.match(r"([a-g]'*\d*)", notes)
        if note_match:

            first_note = note_match.group(1)
            bowed_note = f"{first_note} {bowings[bow_index % 2]}"
            bow_index_local = bow_index  # capture for debugging
            bow_index_nonlocal[0] += 1
            notes = notes.replace(first_note, bowed_note, 1)
        return f"{match.group(1)}{notes}"

    bow_index_nonlocal = [0]
    modified_score = re.sub(slur_pattern, add_bow, score)
    return modified_score

# Apply bowing
bowed_score = insert_bowing(original_score)

# Assemble full LilyPond file
full_lilypond = f"""
\\version "2.24.3"

\\header {{
  title = "pavane"
  instrument = "violon"
}}

global = {{
  \\key g \\major
  \\time 4/4
}}

violin = {bowed_score}

\\score {{
  \\new Staff \\with {{
    instrumentName = "Violon"
    midiInstrument = "violin"
  }} \\violin
  \\layout {{ }}
  \\midi {{
    \\tempo 4=100
  }}
}}
"""

print(full_lilypond)

with open("pavanehey_bowed.ly", "w", encoding="utf-8") as file:
    file.write(full_lilypond)

print("✅ Bowing marks added. Output saved to pavanehey_bowed.ly")
os.system("frescobaldi pavanehey_bowed.ly")

