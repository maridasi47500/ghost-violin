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
  \slurUp (bes16 \downbow  c'8.)
  \slurUp (g'2. ^1 _"D" _"III" \upbow  g'2. ^1 _"D" _"III") r4
  }
  % Mesure 2
  {
    \slurUp (bes16 \downbow  c'8.)
    g'2 ^1 _"D" _"III" \upbow 
    \tuplet 3/2 { \slurUp (bes'8 \downbow  c''8. g'16 ^1 _"D" _"III") }
  }

  % Mesure 3
  {
    \tuplet 3/2 { bes'8 \upbow  f'8 ^1 _"D" _"II" \downbow  g'8 ^1 _"D" _"III" \upbow  }
    \tuplet 3/2 { d'8 ^0 _"D" _"I" \downbow  es'8. \upbow  bes16 \downbow  }
    c'4~ \upbow  
    \tuplet 3/2 { c'8 \downbow  \slurUp (a8 ^1 _"D" _"IV" \upbow  c'8 }
    \tuplet 3/2 { es'8) \slurUp (c'8. \downbow  es'16 }
    \tuplet 3/2 { g'8 ^1 _"D" _"III") \slurUp (es'8 \upbow  g'8 ^1 _"D" _"III") }
    \tuplet 3/2 { a'8 ^1 _"D" _"IV" \downbow  g'8. ^1 _"D" _"III" \upbow  \slurUp (a'16 ^1 _"D" _"IV" \downbow  }
    \tuplet 3/2 { g'8 ^1 _"D" _"III") \slurUp (a'8 ^1 _"D" _"IV" \upbow  g'8 ^1 _"D" _"III") }
    \tuplet 3/2 { a'8 ^1 _"D" _"IV" \downbow  g'8. ^1 _"D" _"III" \upbow  \slurUp (a'16 ^1 _"D" _"IV" \downbow  }
    \tuplet 3/2 { g'8 ^1 _"D" _"III") \slurUp (a'8 ^1 _"D" _"IV" \upbow  g'8 ^1 _"D" _"III") }
  }

  % Mesure 4 — clef treble
  {
    \tuplet 3/2 { \slurUp (bes'8 \downbow  ges'8. bes'16) }
    \slurUp (des''4~ \upbow 
    \tuplet 3/2 { des''8 es''8. c''16) }
    \tuplet 3/2 { des''8 \downbow  bes'8 \upbow  c''8 \downbow  }
    \tuplet 3/2 { \slurUp (as'8 \upbow  bes'8. ges'16) }
    \tuplet 3/2 { as'8 \downbow  f'8 ^1 _"D" _"II" \upbow  ges'8 \downbow  }
  }

  % Mesure 5
  {
    \tuplet 3/2 { \slurUp (f'8 ^1 _"D" _"II" \upbow  d'8. ^0 _"D" _"I" f'16 ^1 _"D" _"II") }
    \tuplet 3/2 { d'8 ^0 _"D" _"I" \downbow  \slurUp (f'8 ^1 _"D" _"II" \upbow  d'8 ^0 _"D" _"I"~) }
    d'8 ^0 _"D" _"I" r8 r4
    
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
