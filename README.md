# Violin Annotation Workflow

- Have `pavanehey.ly` with slur notes and rhythms.

- Run:
  - `python3 slurdownupbow.py 0`  
    - Starts with downbow.
    - Adds alternating bowing marks (`^\downbow`, `^\upbow`).

- Open `pavanehey.ly` in Frescobaldi.

- Select the block that starts with `\relative c'' { ... }`.

- Go to Tools → Pitch → Absolute.

- Frescobaldi rewrites notes using absolute pitch notation.

- Save the result as `pavanehey_absolute.ly`.

- Run:
  - `python3 stringpositionfingering.py`  
    - Adds fingering (`^1`), string (`_"G"`), and position (`_"I"`).

- ✅ Fingering annotations inserted.  
  - Output saved to `violin_annotated.ly`.

# ghost-violin
- 🛠️ Instructions to Use:

 -    there's this script  annotate_violin.sh.

 -   Make it executable:
- chmod +x annotate_violin.sh

 -    bash
- ./annotate_violin.sh

python3 -m venv ~/path/to/venv.
 - source ~/path/to/venv/bin/activate.

![alt text](music1.png)
![alt text](music.png)
