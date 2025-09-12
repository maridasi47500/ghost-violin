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
  \slurUp (g''2 ^2 _"E" _"I" ^\downbow 
  
  g''8 ^2 _"E" _"I" a''8 ^3 _"E" _"I") \slurUp (fis''8 ^\upbow
  e''8 ^4 _"A" _"I") d''4 ^3 _"A" _"I" ^\downbow \slurUp (e''8 ^4 _"A" _"I" ^\upbow fis''8) \slurUp (fis''8 ^\downbow e''8 ^4 _"A" _"I") e''4 ^4 _"A" _"I" ^\upbow \slurUp (b'2 ^1 _"A" _"I" ^\downbow b'8 ^1 _"A" _"I" c''8 ^2 _"A" _"I") \slurUp (a'8 ^4 _"D" _"I" ^\upbow g'8 ^3 _"D" _"I") fis'4 ^\downbow \slurUp (g'8 ^3 _"D" _"I" ^\upbow a'8 ^4 _"D" _"I" a'8 ^4 _"D" _"I" b'8 ^1 _"A" _"I") \slurUp (g'8 ^3 _"D" _"I" ^\downbow fis'8) e'4 ^1 _"D" _"I" ^\upbow \slurUp (fis'8 ^\downbow g'8 ^3 _"D" _"I" g'8 ^3 _"D" _"I" a'8 ^4 _"D" _"I") \slurUp (fis'8 ^\upbow e'8 ^1 _"D" _"I") \slurUp (fis'1 ^\downbow fis'4) \slurUp (b'2 ^1 _"A" _"I" ^\upbow b'4 ^1 _"A" _"I" b'2 ^1 _"A" _"I" b'8 ^1 _"A" _"I" a'8 ^4 _"D" _"I") \slurUp (d''8 ^3 _"A" _"I" ^\downbow b'8 ^1 _"A" _"I") \slurUp (b'4 ^1 _"A" _"I" ^\upbow a'4 ^4 _"D" _"I") \slurUp (g'4 ^3 _"D" _"I" ^\downbow a'4 ^4 _"D" _"I") \slurUp (e'2 ^1 _"D" _"I" ^\upbow e'8 ^1 _"D" _"I" d'8 ^4 _"G" _"I") \slurUp (g'8 ^3 _"D" _"I" ^\downbow fis'8) e'4 ^1 _"D" _"I" ^\upbow b4 ^\downbow d'4 ^4 _"G" _"I" ^\upbow  
  \tuplet 3/2 { \slurUp (c'8 ^3 _"G" _"I" ^\downbow b8 a8) }
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
