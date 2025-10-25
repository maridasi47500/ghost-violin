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

  % Mesure 1
  \slurUp (bes16 \downbow  c'8 ^3 _"G" _"I".)
  \slurUp (g'2 ^3 _"D" _"I". \upbow  g'2 ^3 _"D" _"I".) r4

  % Mesure 2
  {
    \slurUp (bes16 \downbow  c'8 ^3 _"G" _"I".)
    g'2 ^3 _"D" _"I" \upbow 
    \tuplet 3/2 { \slurUp (bes'8 \downbow  c''8 ^2 _"A" _"I". g'16 ^3 _"D" _"I") }
  }

  % Mesure 3
  {
    \tuplet 3/2 { bes8' \upbow  f8 \downbow  g8  \upbow }
    \tuplet 3/2 { d8 \downbow  es8. \upbow  bes,16  \downbow }
    c4~ \upbow  
    \tuplet 3/2 { c8  \downbow \slurUp (a,8 \upbow  c8 }
    \tuplet 3/2 { es8) \slurUp (c8. \downbow  es16 }
    \tuplet 3/2 { g8) \slurUp (es8 \upbow  g8) }
    \tuplet 3/2 { a8 \downbow  g8. \upbow  \slurUp (a16  \downbow }
    \tuplet 3/2 { g8) \slurUp (a8 \upbow  g8) }
    \tuplet 3/2 { a8 \downbow  g8. \upbow  \slurUp (a16  \downbow }
    \tuplet 3/2 { g8) \slurUp (a8 \upbow  g8) }
  }

  % Mesure 4 — clef treble
  \clef treble {
    \tuplet 3/2 { \slurUp (bes'8 \downbow  ges'8. bes'16) }
    \slurUp (des''4~ \upbow 
    \tuplet 3/2 { des''8 es''8. c''16 ^2 _"A" _"I") }
    \tuplet 3/2 { des''8 \downbow  bes'8 \upbow  c''8 ^2 _"A" _"I"  \downbow }
    \tuplet 3/2 { \slurUp (as'8 \upbow  bes'8. ges'16) }
    \tuplet 3/2 { as'8 \downbow  f'8 ^2 _"D" _"I" \upbow  ges'8  \downbow }
  }

  % Mesure 5
  {
    \tuplet 3/2 { \slurUp (f'8 ^2 _"D" _"I" \upbow  d'8 ^4 _"G" _"I". f'16 ^2 _"D" _"I") }
    \tuplet 3/2 { d'8 ^4 _"G" _"I"  \downbow \slurUp (f'8 ^2 _"D" _"I" \upbow  d'8 ^4 _"G" _"I"~) }
    d'8 ^4 _"G" _"I"r8 r4
    
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
