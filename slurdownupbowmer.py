import re

# Load the original LilyPond score
with open("hey-la-mer-partition.ly", "r", encoding="utf-8") as file:
    original_score = file.read()

# Define bowings and index
bowings = ["\\downbow ", "\\upbow "]
bow_index = [0]

# Define note names
note_names = [
    'aes', 'bes', 'ces', 'des', 'ees', 'fes', 'ges',
    'ais', 'bis', 'cis', 'dis', 'eis', 'fis', 'gis',
    'a', 'b', 'c', 'd', 'e', 'f', 'g'
]

# Function to add bowing
def add_bow_to_note(match):
    note = match.group(0)
    bowed_note = f"{note} {bowings[bow_index[0] % 2]}"
    bow_index[0] += 1
    return bowed_note

# Main function
def apply_bowing(score):
    output = ""
    pos = 0
    slur_pattern = re.compile(r"(\\slurUp\s*\()([^\)]+)\)", re.DOTALL)
    note_pattern = '|'.join(sorted(note_names, key=len, reverse=True))

    note_regex = rf"(?<!\w)({note_pattern})'*[0-9]+(.)?(\))?(?!\w)"

    for match in slur_pattern.finditer(score):
        start, end = match.span()
        singles = score[pos:start]
        singles = re.sub(note_regex, add_bow_to_note, singles)
        output += singles

        slur_notes = match.group(2).strip()
        first_note_match = re.match(note_regex, slur_notes)
        if first_note_match:
            first_note = first_note_match.group(0)
            bowed_note = f"{first_note} {bowings[bow_index[0] % 2]}"
            bow_index[0] += 1
            slur_notes = slur_notes.replace(first_note, bowed_note, 1)
        output += f"{match.group(1)}{slur_notes})"
        pos = end

    output += score[pos:]
    return output

# Apply and save
processed_score = apply_bowing(original_score)
with open("pavanehey_bowed.ly", "w", encoding="utf-8") as file:
    file.write(processed_score)

