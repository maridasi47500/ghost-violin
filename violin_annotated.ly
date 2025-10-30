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
  \slurUp (g''2~ ^3 _"E" _"I" \downbow  
  
  g''8 ^3 _"E" _"I" a''8 ^4 _"E" _"I") \slurUp (fis''8 \upbow 
  e''8 ^0 _"E" _"I") d''4 ^4 _"A" _"I" \downbow  \slurUp (e''8 ^0 _"E" _"I" \upbow  fis''8) \slurUp (fis''8 \downbow  e''8 ^0 _"E" _"I") e''4 ^0 _"E" _"I" \upbow  \slurUp (b''2~ \downbow  b''8 c'''8) \slurUp (a''8 ^4 _"E" _"I" \upbow  g''8 ^3 _"E" _"I") fis''4 \downbow  \slurUp (g''8 ^3 _"E" _"I" \upbow  a''8~ ^4 _"E" _"I" a''8 ^4 _"E" _"I" b''8) \slurUp (g''8 ^3 _"E" _"I" \downbow  fis''8) e''4 ^0 _"E" _"I" \upbow  \slurUp (fis''8 \downbow  g''8~ ^3 _"E" _"I" g''8 ^3 _"E" _"I" a''8 ^4 _"E" _"I") \slurUp (fis''8 \upbow  e''8 ^0 _"E" _"I") \slurUp (fis''1 \downbow  fis''4) \slurUp (b''2~ \upbow  b''4~ b''2~ b''8 a''8 ^4 _"E" _"I") \slurUp (d'''8 \downbow  b''8) \slurUp (b''4 \upbow  a''4 ^4 _"E" _"I") \slurUp (g''4 ^3 _"E" _"I" \downbow  a''4 ^4 _"E" _"I") \slurUp (e''2~ ^0 _"E" _"I" \upbow  e''8 ^0 _"E" _"I" d''8 ^4 _"A" _"I") \slurUp (g''8 ^3 _"E" _"I" \downbow  fis''8) e''4 ^0 _"E" _"I" \upbow  b''4 \downbow  d'''4 \upbow   
  \tuplet 3/2 { \slurUp (c'''8 \downbow  b''8 a''8 ^4 _"E" _"I") }
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
