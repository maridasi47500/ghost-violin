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
  \relative c' {
  

  % Mesure 1
  \slurUp (bes16 \downbow  c8.)
  \slurUp (g'2. \upbow  g2.) r4
  }
  % Mesure 2
  \relative c' {
    \slurUp (bes16 \downbow  c8.)
    g'2 \upbow 
    \tuplet 3/2 { \slurUp (bes8 \downbow  c8. g16) }
  }

  % Mesure 3
  \relative c'' {
    \tuplet 3/2 { bes8 \upbow  f8 \downbow  g8 \upbow  }
    \tuplet 3/2 { d8 \downbow  ees8. \upbow  bes16 \downbow  }
    c4~ \upbow  
    \tuplet 3/2 { c8  \slurUp (a8 \downbow  c8 }
    \tuplet 3/2 { ees8) \slurUp (c8. \upbow  ees16 }
    \tuplet 3/2 { g8) \slurUp (ees8 \downbow  g8) }
    \tuplet 3/2 { a8 \upbow  g8. \downbow  \slurUp (a16 \upbow  }
    \tuplet 3/2 { g8) \slurUp (a8 \downbow  g8) }
    \tuplet 3/2 { a8 \upbow  g8. \downbow  \slurUp (a16 \upbow  }
    \tuplet 3/2 { g8) \slurUp (a8 \downbow  g8) }
  }

  % Mesure 4 — clef treble
  \relative c''  {
    \tuplet 3/2 { \slurUp (bes8 \upbow  ges8. bes16) }
    \slurUp (des4~ \downbow 
    \tuplet 3/2 { des8 ees8. c16) }
    \tuplet 3/2 { des8 \upbow  bes8 \downbow  c8 \upbow  }
    \tuplet 3/2 { \slurUp (aes8 \downbow  bes8. ges16) }
    \tuplet 3/2 { aes8 \upbow  f8 \downbow  ges8 \upbow  }
  }

  % Mesure 5
  \relative c' {
    \tuplet 3/2 { \slurUp (f8 \downbow  d8. f16) }
    \tuplet 3/2 { d8 \upbow  \slurUp (f8 \downbow  d8~) }
    d8 r8 r4
    
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
