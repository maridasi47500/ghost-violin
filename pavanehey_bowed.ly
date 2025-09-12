\version "2.24.3"

\header {
  title = "pavane"
  instrument = "violon"
}

global = {
  \key g \major
  \time 4/4
}

violin = \relative c'' {
  \global
  % En avant la musique.
  \slurUp (g'2 ^\downbow 
  
  g8 a8) \slurUp (fis8 ^\upbow
  e8) d4 ^\downbow \slurUp (e8 ^\upbow fis8) \slurUp (fis8 ^\downbow e8) e4 ^\upbow \slurUp (b2 ^\downbow b8 c8) \slurUp (a8 ^\upbow g8) fis4 ^\downbow \slurUp (g8 ^\upbow a8 a8 b8) \slurUp (g8 ^\downbow fis8) e4 ^\upbow \slurUp (fis8 ^\downbow g8 g8 a8) \slurUp (fis8 ^\upbow e8) \slurUp (fis1 ^\downbow fis4) \slurUp (b2 ^\upbow b4 b2 b8 a8) \slurUp (d8 ^\downbow b8) \slurUp (b4 ^\upbow a4) \slurUp (g4 ^\downbow a4) \slurUp (e2 ^\upbow e8 d8) \slurUp (g8 ^\downbow fis8) e4 ^\upbow b4 ^\downbow d4 ^\upbow  
  \tuplet 3/2 { \slurUp (c8 ^\downbow b8 a8) }
  b1
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
