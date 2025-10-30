import re

# Load the original LilyPond score
with open("pavanehey.ly", "r", encoding="utf-8") as file:
    original_score = file.read()
global precedentliaison
precedentliaison=False

# Define bowings and index
bowings = ["\\downbow ", "\\upbow "]
bow_index = [0]
def nth_repl(s,sub, repl, n):
    find = s.find(sub)
    i = find != -1
    while find != -1 and i != n:
        find = s.find(sub, find + 1)
        i+=1
    if i == n:
        return s[:find] + repl + s[find+len(sub):]
    return s

# Define note names
note_names = [

    'aes', 'bes', 'ces', 'des', 'ees', 'fes', 'ges',
    'ais', 'bis', 'cis', 'dis', 'eis', 'fis', 'gis',
    'as', 'bs', 'cs', 'ds', 'es', 'fs', 'gs',
    'a', 'b', 'c', 'd', 'e', 'f', 'g'
]

# Function to add bowing
def add_bow_to_note(match):
    note = match.group(0)

    global precedentliaison
    print(note, precedentliaison)
    precedentliaison=precedentliaison
    if precedentliaison is True:
        bowed_note = f"{note} "
        precedentliaison=False
    else:
        bowed_note = f"{note} {bowings[bow_index[0] % 2]}"
        bow_index[0] += 1
    if "~" in note:
        precedentliaison=True

    #print(note, precedentliaison)




    return bowed_note

# Main function
def apply_bowing(score):
    output = ""
    pos = 0
    slur_pattern = re.compile(r"(\\slurUp\s*\()([^\)]+)\)", re.DOTALL)
    note_pattern = '|'.join(sorted(note_names, key=len, reverse=True))

    #note_regex = rf"(?<!\w)({note_pattern})'*[0-9]+(.)?(\))?(?!\w)"
    my_note_regex = rf"\b(?<!\\relative\s)(({note_pattern})'*([0-9]+)'*(\.)(\~)?)|(\b(?<!\\relative\s)(({note_pattern})'*([0-9]+)'*(\.)(\~)?)(.*)(({note_pattern})'*([0-9]+)'*(\.)?(?<!\~)?))"
    note_regex = rf"\b(?<!\\relative\s)({note_pattern})'*([0-9]+)'*(\.)?(\~)?"
    #slur_regex = rf"\b({note_pattern})'*([0-9]+)'*(\.)?(~).({note_pattern})'*([0-9]+)'(\.)?"

    #for match in slur_regex.finditer(score):
    #    note,height,length,height,dot,liaison,note1,height1,length1,height2,dot= match.span()


    precedentliaison=False
    for match in slur_pattern.finditer(score):
         

        start, end = match.span()
        singles = score[pos:start]
        singles = re.sub(note_regex, add_bow_to_note, singles)

        output += singles

        slur_notes = match.group(2).strip()
        first_note_match = re.match(note_regex, slur_notes)
        if first_note_match and precedentliaison is False:
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

