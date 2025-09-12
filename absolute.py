import re

# Load the absolute-pitch LilyPond score
with open("pavanehey_absolute.ly", "r", encoding="utf-8") as file:
    score = file.read()

# Fingering map: note → (string, finger, position)
fingering_map = {
    # G3 to D4 — G string, 1st position
    "g":    {"string": "G", "finger": "0", "position": "I"},
    "a":    {"string": "G", "finger": "1", "position": "I"},
    "b":    {"string": "G", "finger": "2", "position": "I"},
    "c'":   {"string": "G", "finger": "3", "position": "I"},
    "d'":   {"string": "G", "finger": "4", "position": "I"},

    # D4 to A4 — D string, 1st position
    "d'":   {"string": "D", "finger": "0", "position": "I"},
    "e'":   {"string": "D", "finger": "1", "position": "I"},
    "f'":   {"string": "D", "finger": "2", "position": "I"},
    "g'":   {"string": "D", "finger": "3", "position": "I"},
    "a'":   {"string": "D", "finger": "4", "position": "I"},

    # A4 to E5 — A string, 1st position
    "a'":   {"string": "A", "finger": "0", "position": "I"},
    "b'":   {"string": "A", "finger": "1", "position": "I"},
    "c''":  {"string": "A", "finger": "2", "position": "I"},
    "d''":  {"string": "A", "finger": "3", "position": "I"},
    "e''":  {"string": "A", "finger": "4", "position": "I"},

    # E5 to B5 — E string, 1st position
    "e''":  {"string": "E", "finger": "0", "position": "I"},
    "f''":  {"string": "E", "finger": "1", "position": "I"},
    "g''":  {"string": "E", "finger": "2", "position": "I"},
    "a''":  {"string": "E", "finger": "3", "position": "I"},
    "b''":  {"string": "E", "finger": "4", "position": "I"},

    # D5 to G5 — A string, 3rd position
    "d''_III":  {"string": "A", "finger": "1", "position": "III"},
    "e''_III":  {"string": "A", "finger": "2", "position": "III"},
    "f''_III":  {"string": "A", "finger": "3", "position": "III"},
    "g''_III":  {"string": "A", "finger": "4", "position": "III"},

    # A5 to D6 — E string, 3rd position
    "a''_III":  {"string": "E", "finger": "1", "position": "III"},
    "b''_III":  {"string": "E", "finger": "2", "position": "III"},
    "c'''":     {"string": "E", "finger": "3", "position": "III"},
    "d'''":     {"string": "E", "finger": "4", "position": "III"},

    # E6 — E string, 5th position (optional extension)
    "e'''":     {"string": "E", "finger": "1", "position": "V"},
}


# Annotate each note with correct ordering
def annotate_note(match):
    note = match.group(1)
    duration = match.group(2)
    if note in fingering_map:
        string, finger, position = fingering_map[note]
        return f'{note}{duration} ^{finger} _"{string}" _"{position}"'
    return f"{note}{duration}"

# Regex to match notes with duration (e.g., g''8, a''4)
pattern = r"\b([a-g]'+)(\d+)\b"

# Apply annotations
annotated_score = re.sub(pattern, annotate_note, score)

# Save to new file
with open("pavanehey_fingered.ly", "w", encoding="utf-8") as file:
    file.write(annotated_score)

print("✅ Note durations preserved and annotations applied. Output saved to pavanehey_fingered.ly")

