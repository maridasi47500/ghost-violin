import re
import os

# Load the original LilyPond score
with open("pavanehey.ly", "r", encoding="utf-8") as file:
    original_score = file.read()

# Bowing sequence: alternates continuously
bowings = ["^\\downbow", "^\\upbow"]
bow_index = [0]  # mutable container

# Step 1: Process slurred groups
def process_slurs(score):
    slur_pattern = r"(\\slurUp\s*\()([^\)]+)\)"

    def add_slur_bow(match):
        notes = match.group(2).strip()
        note_match = re.match(r"([a-g]'*\d*)", notes)
        if note_match:
            first_note = note_match.group(1)
            bowed_note = f"{first_note} {bowings[bow_index[0] % 2]}"
            bow_index[0] += 1
            notes = notes.replace(first_note, bowed_note, 1)
        return f"{match.group(1)}{notes})"

    return re.sub(slur_pattern, add_slur_bow, score)

# Step 2: Process single notes (outside slurs)
def process_singles(score):
    # Temporarily remove slur groups to avoid double bowing
    slur_pattern = r"(\\slurUp\s*\([^\)]+\))"
    slurs = re.findall(slur_pattern, score)
    score_clean = re.sub(slur_pattern, "§§SLUR§§", score)

    # Add bowing to single notes
    def add_single_bow(match):
        note = match.group(1)
        bowed_note = f"{note} {bowings[bow_index[0] % 2]}"
        bow_index[0] += 1
        return bowed_note

    score_clean = re.sub(r"\b([a-g]'*\d+)\b", add_single_bow, score_clean)

    # Restore slur groups
    for slur in slurs:
        score_clean = score_clean.replace("§§SLUR§§", slur, 1)

    return score_clean

# Apply transformations
score_with_slurs = process_slurs(original_score)
final_score = process_singles(score_with_slurs)

# Write to output file
with open("pavanehey_bowed.ly", "w", encoding="utf-8") as file:
    file.write(final_score)

print("✅ Bowing applied with continuous alternation across slurs and single notes. Output saved to pavanehey_bowed.ly")

os.system("frescobaldi pavanehey_bowed.ly")

