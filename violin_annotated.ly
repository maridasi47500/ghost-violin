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
  \slurUp (g''2~ ^2 _"E" _"I" \downbow  
  
  g''8 ^2 _"E" _"I" a''8 ^1 _"E" _"III") \slurUp (fis''8 ^1 _"E" _"I" \upbow 
  e''8 ^0 _"E" _"I") d''4 ^3 _"A" _"I" \downbow  \slurUp (e''8 ^0 _"E" _"I" \upbow  fis''8 ^1 _"E" _"I") \slurUp (fis''8 ^1 _"E" _"I" \downbow  e''8 ^0 _"E" _"I") e''4 ^0 _"E" _"I" \upbow  \slurUp (b''2~ ^2 _"E" _"III" \downbow  b''8 ^2 _"E" _"III" c'''8 ^3 _"E" _"III") \slurUp (a''8 ^1 _"E" _"III" \upbow  g''8 ^2 _"E" _"I") fis''4 ^1 _"E" _"I" \downbow  \slurUp (g''8 ^2 _"E" _"I" \upbow  a''8~ ^1 _"E" _"III" a''8 ^1 _"E" _"III" b''8 ^2 _"E" _"III") \slurUp (g''8 ^2 _"E" _"I" \downbow  fis''8 ^1 _"E" _"I") e''4 ^0 _"E" _"I" \upbow  \slurUp (fis''8 ^1 _"E" _"I" \downbow  g''8~ ^2 _"E" _"I" g''8 ^2 _"E" _"I" a''8 ^1 _"E" _"III") \slurUp (fis''8 ^1 _"E" _"I" \upbow  e''8 ^0 _"E" _"I") \slurUp (fis''1 ^1 _"E" _"I" \downbow  fis''4 ^1 _"E" _"I") \slurUp (b''2~ ^2 _"E" _"III" \upbow  b''4~ ^2 _"E" _"III" b''2~ ^2 _"E" _"III" b''8 ^2 _"E" _"III" a''8 ^1 _"E" _"III") \slurUp (d'''8 ^4 _"E" _"III" \downbow  b''8 ^2 _"E" _"III") \slurUp (b''4 ^2 _"E" _"III" \upbow  a''4 ^1 _"E" _"III") \slurUp (g''4 ^2 _"E" _"I" \downbow  a''4 ^1 _"E" _"III") \slurUp (e''2~ ^0 _"E" _"I" \upbow  e''8 ^0 _"E" _"I" d''8 ^3 _"A" _"I") \slurUp (g''8 ^2 _"E" _"I" \downbow  fis''8 ^1 _"E" _"I") e''4 ^0 _"E" _"I" \upbow  b''4 ^2 _"E" _"III" \downbow  d'''4 ^4 _"E" _"III" \upbow   
  \tuplet 3/2 { \slurUp (c'''8 ^3 _"E" _"III" \downbow  b''8 ^2 _"E" _"III" a''8 ^1 _"E" _"III") }
  b''1 ^2 _"E" _"III"
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
