\version "2.24.3"

\header {
  title = "pavane"
  instrument = "violon"
}

global = {
  \key g \major
  \time 4/4
}

violin = {
  \global
  % En avant la musique.
  \slurUp (g''2~ \downbow  
  
  g''8 a''8) \slurUp (fis''8 \upbow 
  e''8) d''4 \downbow  \slurUp (e''8 \upbow  fis''8) \slurUp (fis''8 \downbow  e''8) e''4 \upbow  \slurUp (b''2~ \downbow  b''8 c'''8) \slurUp (a''8 \upbow  g''8) fis''4 \downbow  \slurUp (g''8 \upbow  a''8~ a''8 b''8) \slurUp (g''8 \downbow  fis''8) e''4 \upbow  \slurUp (fis''8 \downbow  g''8~ g''8 a''8) \slurUp (fis''8 \upbow  e''8) \slurUp (fis''1 \downbow  fis''4) \slurUp (b''2~ \upbow  b''4~ b''2~ b''8 a''8) \slurUp (d'''8 \downbow  b''8) \slurUp (b''4 \upbow  a''4) \slurUp (g''4 \downbow  a''4) \slurUp (e''2~ \upbow  e''8 d''8) \slurUp (g''8 \downbow  fis''8) e''4 \upbow  b''4 \downbow  d'''4 \upbow   
  \tuplet 3/2 { \slurUp (c'''8 \downbow  b''8 a''8) }
  b''1
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
