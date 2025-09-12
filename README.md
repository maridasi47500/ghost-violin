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
