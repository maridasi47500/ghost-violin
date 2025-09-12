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
  \slurUp (g''2 ^finger _"string" _"position" ^\downbow 
  
  g''8 ^finger _"string" _"position" a''8 ^finger _"string" _"position") \slurUp (f''8 ^finger _"string" _"position" ^\upbow
  e''8 ^finger _"string" _"position") d''4 ^finger _"string" _"position" ^\downbow \slurUp (e''8 ^finger _"string" _"position" ^\upbow f''8 ^finger _"string" _"position") \slurUp (f''8 ^finger _"string" _"position" ^\downbow e''8 ^finger _"string" _"position") e''4 ^finger _"string" _"position" ^\upbow \slurUp (b'2 ^finger _"string" _"position" ^\downbow b'8 ^finger _"string" _"position" c''8 ^finger _"string" _"position") \slurUp (a'8 ^finger _"string" _"position" ^\upbow g'8 ^finger _"string" _"position") f'4 ^finger _"string" _"position" ^\downbow \slurUp (g'8 ^finger _"string" _"position" ^\upbow a'8 ^finger _"string" _"position" a'8 ^finger _"string" _"position" b'8 ^finger _"string" _"position") \slurUp (g'8 ^finger _"string" _"position" ^\downbow f'8 ^finger _"string" _"position") e'4 ^finger _"string" _"position" ^\upbow \slurUp (f'8 ^finger _"string" _"position" ^\downbow g'8 ^finger _"string" _"position" g'8 ^finger _"string" _"position" a'8 ^finger _"string" _"position") \slurUp (f'8 ^finger _"string" _"position" ^\upbow e'8 ^finger _"string" _"position") \slurUp (f'1 ^finger _"string" _"position" ^\downbow f'4 ^finger _"string" _"position") \slurUp (b'2 ^finger _"string" _"position" ^\upbow b'4 ^finger _"string" _"position" b'2 ^finger _"string" _"position" b'8 ^finger _"string" _"position" a'8 ^finger _"string" _"position") \slurUp (d''8 ^finger _"string" _"position" ^\downbow b'8 ^finger _"string" _"position") \slurUp (b'4 ^finger _"string" _"position" ^\upbow a'4 ^finger _"string" _"position") \slurUp (g'4 ^finger _"string" _"position" ^\downbow a'4 ^finger _"string" _"position") \slurUp (e'2 ^finger _"string" _"position" ^\upbow e'8 ^finger _"string" _"position" d'8 ^finger _"string" _"position") \slurUp (g'8 ^finger _"string" _"position" ^\downbow f'8 ^finger _"string" _"position") e'4 ^finger _"string" _"position" ^\upbow b4 ^\downbow d'4 ^finger _"string" _"position" ^\upbow  
  \tuplet 3/2 { \slurUp (c'8 ^finger _"string" _"position" ^\downbow b8 a8) }
  b1 ^\upbow
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
