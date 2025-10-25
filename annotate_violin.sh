#!/bin/bash

# 🎻 Violin Annotation Workflow Script

# Step 1: Add alternating bowing marks
echo "➤ Adding bowing marks to pavanehey.ly..."
python3 slurdownupbowmer.py 0
echo "✅ Bowing marks added."

# Step 2: Convert to absolute pitch using Frescobaldi
echo "➤ Please open pavanehey_bowed.ly in Frescobaldi."
echo "   Select the block starting with \\relative c'' { ... }"
echo "   Then go to Tools → Pitch → Absolute."
echo "   Save the result as pavanehey_absolute.ly"
read -p "⏸️ Press Enter once you've completed this step in Frescobaldi..."

# Step 3: Add fingering, string, and position annotations
echo "➤ Adding fingering, string, and position annotations..."
python3 stringpositionfingering.py
echo "✅ Annotations inserted. Output saved to violin_annotated.ly."

