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
  \slurUp (g'2. \upbow  g'2.) r4
  }
  % Mesure 2
  {
    \slurUp (bes16 \downbow  c'8.)
    g'2 \upbow 
    \tuplet 3/2 { \slurUp (bes'8 \downbow  c''8. g'16) }
  }

  % Mesure 3
  {
    \tuplet 3/2 { bes'8 \upbow  f'8 \downbow  g'8 \upbow  }
    \tuplet 3/2 { d'8 \downbow  es'8. \upbow  bes16 \downbow  }
    c'4~ \upbow  
    \tuplet 3/2 { c'8  \slurUp (a8 \downbow  c'8 }
    \tuplet 3/2 { es'8) \slurUp (c'8. \upbow  es'16 }
    \tuplet 3/2 { g'8) \slurUp (es'8 \downbow  g'8) }
    \tuplet 3/2 { a'8 \upbow  g'8. \downbow  \slurUp (a'16 \upbow  }
    \tuplet 3/2 { g'8) \slurUp (a'8 \downbow  g'8) }
    \tuplet 3/2 { a'8 \upbow  g'8. \downbow  \slurUp (a'16 \upbow  }
    \tuplet 3/2 { g'8) \slurUp (a'8 \downbow  g'8) }
  }

  % Mesure 4 — clef treble
  {
    \tuplet 3/2 { \slurUp (bes'8 \upbow  ges'8. bes'16) }
    \slurUp (des''4~ \downbow 
    \tuplet 3/2 { des''8 es''8. c''16) }
    \tuplet 3/2 { des''8 \upbow  bes'8 \downbow  c''8 \upbow  }
    \tuplet 3/2 { \slurUp (as'8 \downbow  bes'8. ges'16) }
    \tuplet 3/2 { as'8 \upbow  f'8 \downbow  ges'8 \upbow  }
  }

  % Mesure 5
  {
    \tuplet 3/2 { \slurUp (f'8 \downbow  d'8. f'16) }
    \tuplet 3/2 { d'8 \upbow  \slurUp (f'8 \downbow  d'8~) }
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
