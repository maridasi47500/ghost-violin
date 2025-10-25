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
  \slurUp (bes16 \downbow  c'8.)
  \slurUp (g'2. \upbow  g'2.) r4

  % Mesure 2
  {
    \slurUp (bes16 \downbow  c'8.)
    g'2 \upbow 
    \tuplet 3/2 { \slurUp (bes'8 \downbow  c''8. g'16) }
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
    \tuplet 3/2 { des''8 es''8. c''16) }
    \tuplet 3/2 { des''8 \downbow  bes'8 \upbow  c''8  \downbow }
    \tuplet 3/2 { \slurUp (as'8 \upbow  bes'8. ges'16) }
    \tuplet 3/2 { as'8 \downbow  f'8 \upbow  ges'8  \downbow }
  }

  % Mesure 5
  {
    \tuplet 3/2 { \slurUp (f'8 \upbow  d'8. f'16) }
    \tuplet 3/2 { d'8  \downbow \slurUp (f'8 \upbow  d'8~) }
    d'8 r8 r4
    
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
