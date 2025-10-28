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
fingering_map={'g': {'string': 'G', 'position': 'I', 'finger': '0'}, 'ais': {'string': 'G', 'position': 'I', 'finger': '1'}, 'a': {'string': 'G', 'position': 'I', 'finger': '1'}, 'bes': {'string': 'G', 'position': 'II', 'finger': '1'}, 'b': {'string': 'G', 'position': 'II', 'finger': '1'}, "c'": {'string': 'G', 'position': 'III', 'finger': '1'}, "cis'": {'string': 'G', 'position': 'III', 'finger': '1'}, "d'": {'string': 'D', 'position': 'I', 'finger': '0'}, "ees'": {'string': 'D', 'position': 'I', 'finger': '1'}, "e'": {'string': 'D', 'position': 'I', 'finger': '1'}, "f'": {'string': 'D', 'position': 'II', 'finger': '1'}, "fis'": {'string': 'D', 'position': 'II', 'finger': '1'}, "g'": {'string': 'D', 'position': 'III', 'finger': '1'}, "ais'": {'string': 'D', 'position': 'III', 'finger': '1'}, "a'": {'string': 'A', 'position': 'I', 'finger': '0'}, "bes'": {'string': 'A', 'position': 'I', 'finger': '1'}, "b'": {'string': 'A', 'position': 'I', 'finger': '1'}, "c''": {'string': 'A', 'position': 'II', 'finger': '1'}, "cis''": {'string': 'A', 'position': 'II', 'finger': '1'}, "d''": {'string': 'A', 'position': 'III', 'finger': '1'}, "ees''": {'string': 'A', 'position': 'IV', 'finger': '1'}, "e''": {'string': 'E', 'position': 'I', 'finger': '0'}, "f''": {'string': 'E', 'position': 'I', 'finger': '1'}, "fis''": {'string': 'E', 'position': 'I', 'finger': '1'}, "g''": {'string': 'E', 'position': 'II', 'finger': '1'}, "ais''": {'string': 'E', 'position': 'II', 'finger': '1'}, "a''": {'string': 'E', 'position': 'III', 'finger': '1'}, "bes''": {'string': 'E', 'position': 'IV', 'finger': '1'}, "b''": {'string': 'E', 'position': 'IV', 'finger': '1'}, "c'''": {'string': 'E', 'position': 'V', 'finger': '1'}, "cis'''": {'string': 'E', 'position': 'V', 'finger': '1'}, "d'''": {'string': 'E', 'position': 'VI', 'finger': '1'}, "ees'''": {'string': 'E', 'position': 'VII', 'finger': '1'}, "e'''": {'string': 'E', 'position': 'VII', 'finger': '1'}, "f'''": {'string': 'E', 'position': 'VIII', 'finger': '1'}, "fis'''": {'string': 'E', 'position': 'VIII', 'finger': '1'}}




# Load the LilyPond fragment
with open("pavanehey_absolute.ly", "r", encoding="utf-8") as file:
    score = file.read()

# Replace placeholders with actual fingering data
def replace_placeholders(match):
    print(match)
    note = match.group(1)
    try:
        hey = match.group(2)
    except:
        hey = ""
    try:
        height = match.group(3)
    except:
        height = ""
    try:
        duration = match.group(4)
    except:
        duration = ""

    try:
        dot = match.group(5)
    except:
        dot = ""
    if note is None:
        note = ""
    if height is None:
        height = ""
    if duration is None:
        duration = ""
    if hey is None:
        hey = ""
    if dot is None:
        dot = ""
    #print(note,height,duration,hey,dot)
    key = note+height
    if key not in fingering_map:
        print(f"{note}{hey}{height}{duration}{dot}")
        return f"{note}{height}{duration}{dot}"  # leave unannotated if not found
    data = fingering_map[key]
    print(f'{note}{hey}{height}{duration}{dot} ^{data["finger"]} _"{data["string"]}" _"{data["position"]}"')
    return f'{note}{height}{duration}{dot} ^{data["finger"]} _"{data["string"]}" _"{data["position"]}"'

# Match notes with duration (e.g., g''8, a'4)
####pattern = r"\b([a-g]'+)(\d+)(.)?\b"
note_names = [
    'aes', 'bes', 'ces', 'des', 'ees', 'fes', 'ges',
    'ais', 'bis', 'cis', 'dis', 'eis', 'fis', 'gis',
    'as', 'bs', 'cs', 'ds', 'es', 'fs', 'gs',

    'a', 'b', 'c', 'd', 'e', 'f', 'g'
]

note_pattern = '|'.join(sorted(note_names, key=len, reverse=True))


#pattern = rf"\b(?<!\\relative\s)({note_pattern})(,+)?('+)?(\d+)(\.)?"
pattern = rf"\b({note_pattern})(,+)?('+)?(\d+)(\.)?"


# Apply replacements
annotated_score = re.sub(pattern, replace_placeholders, score)

# Save to output file
with open("violin_annotated.ly", "w", encoding="utf-8") as file:
    file.write(annotated_score)

print("✅ Fingering annotations inserted. Output saved to violin_annotated.ly")

