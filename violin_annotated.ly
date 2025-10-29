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
  \slurUp (bes16 ^3 _"G" _"I" \downbow  c'8. ^4 _"G" _"I")
  \slurUp (g'2. ^3 _"D" _"I" \upbow  g'2. ^3 _"D" _"I") r4
  }
  % Mesure 2
  {
    \slurUp (bes16 ^3 _"G" _"I" \downbow  c'8. ^4 _"G" _"I")
    g'2 ^3 _"D" _"I" \upbow 
    \tuplet 3/2 { \slurUp (bes'8 ^1 _"A" _"I" \downbow  c''8. ^2 _"A" _"I" g'16 ^3 _"D" _"I") }
  }

  % Mesure 3
  {
    \tuplet 3/2 { bes'8 ^1 _"A" _"I" \upbow  f'8 ^2 _"D" _"I" \downbow  g'8 ^3 _"D" _"I" \upbow  }
    \tuplet 3/2 { d'8 ^0 _"D" _"I" \downbow  ees'8. ^1 _"D" _"I" \upbow  bes16 ^3 _"G" _"I" \downbow  }
    c'4~ ^4 _"G" _"I" \upbow  
    \tuplet 3/2 { c'8 ^4 _"G" _"I"  \slurUp (a8 ^2 _"G" _"I" \downbow  c'8 ^4 _"G" _"I" }
    \tuplet 3/2 { ees'8 ^1 _"D" _"I") \slurUp (c'8. ^4 _"G" _"I" \upbow  ees'16 ^1 _"D" _"I" }
    \tuplet 3/2 { g'8 ^3 _"D" _"I") \slurUp (ees'8 ^1 _"D" _"I" \downbow  g'8 ^3 _"D" _"I") }
    \tuplet 3/2 { a'8 ^0 _"A" _"I" \upbow  g'8. ^3 _"D" _"I" \downbow  \slurUp (a'16 ^0 _"A" _"I" \upbow  }
    \tuplet 3/2 { g'8 ^3 _"D" _"I") \slurUp (a'8 ^0 _"A" _"I" \downbow  g'8 ^3 _"D" _"I") }
    \tuplet 3/2 { a'8 ^0 _"A" _"I" \upbow  g'8. ^3 _"D" _"I" \downbow  \slurUp (a'16 ^0 _"A" _"I" \upbow  }
    \tuplet 3/2 { g'8 ^3 _"D" _"I") \slurUp (a'8 ^0 _"A" _"I" \downbow  g'8 ^3 _"D" _"I") }
  }

  % Mesure 4 — clef treble
  {
    \tuplet 3/2 { \slurUp (bes'8 ^1 _"A" _"I" \upbow  ges'8. ^2 _"D" _"I" bes'16 ^1 _"A" _"I") }
    \slurUp (des''4~ ^2 _"A" _"I" \downbow 
    \tuplet 3/2 { des''8 ^2 _"A" _"I" ees''8. ^4 _"A" _"I" c''16 ^2 _"A" _"I") }
    \tuplet 3/2 { des''8 ^2 _"A" _"I" \upbow  bes'8 ^1 _"A" _"I" \downbow  c''8 ^2 _"A" _"I" \upbow  }
    \tuplet 3/2 { \slurUp (aes'8 ^3 _"D" _"I" \downbow  bes'8. ^1 _"A" _"I" ges'16 ^2 _"D" _"I") }
    \tuplet 3/2 { aes'8 ^3 _"D" _"I" \upbow  f'8 ^2 _"D" _"I" \downbow  ges'8 ^2 _"D" _"I" \upbow  }
  }

  % Mesure 5
  {
    \tuplet 3/2 { \slurUp (f'8 ^2 _"D" _"I" \downbow  d'8. ^0 _"D" _"I" f'16 ^2 _"D" _"I") }
    \tuplet 3/2 { d'8 ^0 _"D" _"I" \upbow  \slurUp (f'8 ^2 _"D" _"I" \downbow  d'8~ ^0 _"D" _"I") }
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
