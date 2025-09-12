import re

# Load the absolute-pitch LilyPond score
with open("pavanehey_absolute.ly", "r", encoding="utf-8") as file:
    score = file.read()

# Fingering map: note → (string, finger, position)
fingering_map = {
    "g'": ("G", "open", "1st"),
    "a'": ("G", "1st", "1st"),
    "b'": ("G", "2nd", "1st"),
    "c''": ("G", "4th", "1st"),
    "d''": ("D", "open", "1st"),
    "e''": ("D", "1st", "1st"),
    "f''": ("D", "2nd", "1st"),
    "g''": ("D", "3rd", "1st"),
    "a''": ("A", "1st", "3rd"),
    "b''": ("A", "2nd", "3rd"),
    "c'''": ("A", "3rd", "3rd"),
    "d'''": ("A", "4th", "3rd"),
    "e'''": ("E", "1st", "3rd"),
    "f'''": ("E", "2nd", "3rd"),
    "g'''": ("E", "3rd", "3rd"),
}

# Annotate each note with fingering
def annotate_fingering(score):
    def add_markup(match):
        note = match.group(1)
        if note in fingering_map:
            string, finger, position = fingering_map[note]
            markup = f'^\\markup {{ "{string} string, {finger} finger, {position} pos" }}'
            return f"{note} {markup}"
        return note
    return re.sub(r"\b([a-g]'+)\b", add_markup, score)

# Apply annotations
annotated_score = annotate_fingering(score)

# Save to new file
with open("pavanehey_fingered.ly", "w", encoding="utf-8") as file:
    file.write(annotated_score)

print("✅ Fingering annotations added. Output saved to pavanehey_fingered.ly")

