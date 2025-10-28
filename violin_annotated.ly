\version "2.20.0"

\header {
  title = "la mer"
  composer = "hey"
}

global = {
  \clef treble
  \key bes \major
  \time 4/4
}

violin = {
  
  \global
  {
  

  % Mesure 1
  \slurUp (bes16 ^1 _"G" _"II" \downbow  c'8. ^1 _"A" _"II")
  \slurUp (g'2. ^1 _"D" _"III" \upbow  g'2. ^1 _"D" _"III") r4
  }
  % Mesure 2
  {
    \slurUp (bes16 ^1 _"G" _"II" \downbow  c'8. ^1 _"A" _"II")
    g'2 ^1 _"D" _"III" \upbow 
    \tuplet 3/2 { \slurUp (bes'8 ^1 _"A" _"I" \downbow  c''8. ^1 _"E" _"V" g'16 ^1 _"D" _"III") }
  }

  % Mesure 3
  {
    \tuplet 3/2 { bes'8 ^1 _"A" _"I" \upbow  f'8 ^1 _"D" _"II" \downbow  g'8 ^1 _"D" _"III" \upbow  }
    \tuplet 3/2 { d'8 ^1 _"A" _"III" \downbow  es'8. \upbow  bes16 ^1 _"G" _"II" \downbow  }
    c'4 ^1 _"A" _"II"~ \upbow  
    \tuplet 3/2 { c'8 ^1 _"A" _"II" \downbow  \slurUp (a8 ^1 _"G" _"I" \upbow  c'8 ^1 _"A" _"II" }
    \tuplet 3/2 { es'8) \slurUp (c'8. ^1 _"A" _"II" \downbow  es'16 }
    \tuplet 3/2 { g'8 ^1 _"D" _"III") \slurUp (es'8 \upbow  g'8 ^1 _"D" _"III") }
    \tuplet 3/2 { a'8 ^0 _"A" _"I" \downbow  g'8. ^1 _"D" _"III" \upbow  \slurUp (a'16 ^0 _"A" _"I" \downbow  }
    \tuplet 3/2 { g'8 ^1 _"D" _"III") \slurUp (a'8 ^0 _"A" _"I" \upbow  g'8 ^1 _"D" _"III") }
    \tuplet 3/2 { a'8 ^0 _"A" _"I" \downbow  g'8. ^1 _"D" _"III" \upbow  \slurUp (a'16 ^0 _"A" _"I" \downbow  }
    \tuplet 3/2 { g'8 ^1 _"D" _"III") \slurUp (a'8 ^0 _"A" _"I" \upbow  g'8 ^1 _"D" _"III") }
  }

  % Mesure 4 — clef treble
  {
    \tuplet 3/2 { \slurUp (bes'8 ^1 _"A" _"I" \downbow  ges'8. bes'16 ^1 _"A" _"I") }
    \slurUp (des''4~ \upbow 
    \tuplet 3/2 { des''8 es''8. c''16 ^1 _"E" _"V") }
    \tuplet 3/2 { des''8 \downbow  bes'8 ^1 _"A" _"I" \upbow  c''8 ^1 _"E" _"V" \downbow  }
    \tuplet 3/2 { \slurUp (as'8 \upbow  bes'8. ^1 _"A" _"I" ges'16) }
    \tuplet 3/2 { as'8 \downbow  f'8 ^1 _"D" _"II" \upbow  ges'8 \downbow  }
  }

  % Mesure 5
  {
    \tuplet 3/2 { \slurUp (f'8 ^1 _"D" _"II" \upbow  d'8. ^1 _"A" _"III" f'16 ^1 _"D" _"II") }
    \tuplet 3/2 { d'8 ^1 _"A" _"III" \downbow  \slurUp (f'8 ^1 _"D" _"II" \upbow  d'8 ^1 _"A" _"III"~) }
    d'8 ^1 _"A" _"III" r8 r4
    
  }
}

\score {
  \new Staff \with {
    instrumentName = "Violon"
    midiInstrument = "violin"
  } \violin

  \layout { }
  \midi {
    \tempo 4=100
  }
}
