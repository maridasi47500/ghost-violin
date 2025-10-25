import re

# Fingering map: note → {string, finger, position}
fingering_map = {
    # G string
    "g":    {"string": "G", "finger": "0", "position": "I"},
    "a":    {"string": "G", "finger": "1", "position": "I"},
    "b":    {"string": "G", "finger": "2", "position": "I"},
    "c'":   {"string": "G", "finger": "3", "position": "I"},
    "d'":   {"string": "G", "finger": "4", "position": "I"},

    # D string
    "e'":   {"string": "D", "finger": "1", "position": "I"},
    "f'":   {"string": "D", "finger": "2", "position": "I"},
    "g'":   {"string": "D", "finger": "3", "position": "I"},
    "a'":   {"string": "D", "finger": "4", "position": "I"},

    # A string
    "b'":   {"string": "A", "finger": "1", "position": "I"},
    "c''":  {"string": "A", "finger": "2", "position": "I"},
    "d''":  {"string": "A", "finger": "3", "position": "I"},
    "e''":  {"string": "A", "finger": "4", "position": "I"},

    # E string
    "f''":  {"string": "E", "finger": "1", "position": "I"},
    "g''":  {"string": "E", "finger": "2", "position": "I"},
    "a''":  {"string": "E", "finger": "3", "position": "I"},
    "b''":  {"string": "E", "finger": "4", "position": "I"},

    # 3rd position on A string
    "d''_III": {"string": "A", "finger": "1", "position": "III"},
    "e''_III": {"string": "A", "finger": "2", "position": "III"},
    "f''_III": {"string": "A", "finger": "3", "position": "III"},
    "g''_III": {"string": "A", "finger": "4", "position": "III"},

    # 3rd position on E string
    "a''_III": {"string": "E", "finger": "1", "position": "III"},
    "b''_III": {"string": "E", "finger": "2", "position": "III"},
    "c'''":    {"string": "E", "finger": "3", "position": "III"},
    "d'''":    {"string": "E", "finger": "4", "position": "III"},
    "e'''":    {"string": "E", "finger": "1", "position": "V"},
}

# Load the LilyPond fragment
with open("pavanehey_absolute.ly", "r", encoding="utf-8") as file:
    score = file.read()

# Replace placeholders with actual fingering data
def replace_placeholders(match):
    note = match.group(1)
    duration = match.group(2)
    key = note
    if key not in fingering_map:
        return f"{note}{duration}"  # leave unannotated if not found
    data = fingering_map[key]
    return f'{note}{duration} ^{data["finger"]} _"{data["string"]}" _"{data["position"]}"'

# Match notes with duration (e.g., g''8, a'4)
pattern = r"\b([a-g]'+)(\d+)(.)?\b"

# Apply replacements
annotated_score = re.sub(pattern, replace_placeholders, score)

# Save to output file
with open("violin_annotated.ly", "w", encoding="utf-8") as file:
    file.write(annotated_score)

print("✅ Fingering annotations inserted. Output saved to violin_annotated.ly")

