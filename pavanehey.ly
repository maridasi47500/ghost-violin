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
  \slurUp (g'2 
  
  g8 a8) \slurUp (f8
  e8) d4 \slurUp (e8 f8) \slurUp (f8 e8) e4 \slurUp (b2 b8 c8) \slurUp (a8 g8) f4 \slurUp (g8 a8 a8 b8) \slurUp (g8 f8) e4 \slurUp (f8 g8 g8 a8) \slurUp (f8 e8) \slurUp (f1 f4) \slurUp (b2 b4 b2 b8 a8) \slurUp (d8 b8) \slurUp (b4 a4) \slurUp (g4 a4) \slurUp (e2 e8 d8) \slurUp (g8 f8) e4 b4 d4  
  \tuplet 3/2 { \slurUp (c8 b8 a8) }
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
