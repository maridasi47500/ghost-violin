import re
import os

# Load the original LilyPond score
with open("pavanehey.ly", "r", encoding="utf-8") as file:
    original_score = file.read()

# Bowing sequence: alternates continuously
bowings = ["^\\downbow", "^\\upbow"]
bow_index = [0]  # mutable container

# Combined processing of slurs and singles
def apply_bowing(score):
    output = ""
    pos = 0

    # Pattern to find slur groups
    slur_pattern = re.compile(r"(\\slurUp\s*\()([^\)]+)\)", re.DOTALL)

    for match in slur_pattern.finditer(score):
        start, end = match.span()
        # Process content before this slur (single notes)
        singles = score[pos:start]
        singles = re.sub(r"\b([a-g]'*\d+)\b", add_bow_to_note, singles)
        output += singles

        # Process the slur group
        slur_notes = match.group(2).strip()
        first_note_match = re.match(r"([a-g]'*\d*)", slur_notes)
        if first_note_match:
            first_note = first_note_match.group(1)
            bowed_note = f"{first_note} {bowings[bow_index[0] % 2]}"
            bow_index[0] += 1
            slur_notes = slur_notes.replace(first_note, bowed_note, 1)
        output += f"{match.group(1)}{slur_notes})"
        pos = end

    # Process remaining content after last slur
    remaining = score[pos:]
    remaining = re.sub(r"\b([a-g]'*\d+)\b", add_bow_to_note, remaining)
    output += remaining

    return output

# Helper to add bowing to single notes
def add_bow_to_note(match):
    note = match.group(1)
    bowed_note = f"{note} {bowings[bow_index[0] % 2]}"
    bow_index[0] += 1
    return bowed_note

# Apply bowing
final_score = apply_bowing(original_score)

# Write to output file
with open("pavanehey_bowed.ly", "w", encoding="utf-8") as file:
    file.write(final_score)

print("✅ Bowing applied with seamless alternation across slurs and single notes.")
os.system("frescobaldi pavanehey_bowed.ly")

