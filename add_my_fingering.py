import re

# Load the absolute-pitch LilyPond score
with open("pavanehey_absolute.ly", "r", encoding="utf-8") as file:
    score = file.read()

# Fingering map: note → (string, finger, position)
fingering_map = {
    "g'":  ("G", "0", "I"),
    "a'":  ("G", "1", "I"),
    "b'":  ("G", "2", "I"),
    "c''": ("G", "4", "I"),
    "d''": ("D", "0", "I"),
    "e''": ("D", "1", "I"),
    "f''": ("D", "2", "I"),
    "g''": ("D", "3", "I"),
    "a''": ("A", "1", "III"),
    "b''": ("A", "2", "III"),
    "c'''":("A", "3", "III"),
    "d'''":("A", "4", "III"),
    "e'''":("E", "1", "III"),
    "f'''":("E", "2", "III"),
    "g'''":("E", "3", "III"),
}

# Annotate each note with fingering, string, and position
def annotate_note(match):
    note = match.group(1)
    if note in fingering_map:
        string, finger, position = fingering_map[note]
        return f'{note} ^{finger} _"{string}" _"{position}"'
    return note

# Apply annotations
annotated_score = re.sub(r"\b([a-g]'+)\b", annotate_note, score)

# Save to new file
with open("pavanehey_fingered.ly", "w", encoding="utf-8") as file:
    file.write(annotated_score)

print("✅ Fingering, string, and position annotations added. Output saved to pavanehey_fingered.ly")

