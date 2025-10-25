\version "2.20.0"

\header {
  title = "la mer"
  composer = "hey"
}

global = {
  \clef tenor
  \key bes \major
  \time 4/4
}

violin = {
  \global

  % Mesure 1
  \slurUp (b16 ^\upbow c'8.)
  \slurUp (g'2 ^\downbow. g'2.) r4

  % Mesure 2
  {
    \slurUp (b16 ^\upbow c'8.)
    g'2 ^\downbow
    \tuplet 3/2 { \slurUp (b'8 ^\upbow c''8. g'16) }
  }

  % Mesure 3
  {
    \tuplet 3/2 { b8 ^\downbow' f8 ^\upbow g8 ^\downbow }
    \tuplet 3/2 { d8 ^\upbow e8 ^\downbow b,8 ^\upbow }
    c4 ^\downbow~ 
    \tuplet 3/2 { c8 ^\upbow \slurUp (a,8 ^\downbow c8 }
    \tuplet 3/2 { e8) \slurUp (c8 ^\upbow e8 }
    \tuplet 3/2 { g8) \slurUp (e8 ^\downbow g8) }
    \tuplet 3/2 { a8 ^\upbow. g16 ^\downbow \slurUp (a8 ^\upbow }
    \tuplet 3/2 { g8) \slurUp (a8 ^\downbow g8) }
    \tuplet 3/2 { a8 ^\upbow. g16 ^\downbow \slurUp (a8 ^\upbow }
    \tuplet 3/2 { g8) \slurUp (a8 ^\downbow g8) }
  }

  % Mesure 4 — clef treble
  \clef treble {
    \tuplet 3/2 { \slurUp (bes'8 ^\upbow ges'8. bes'16) }
    \slurUp (des''4 ^\downbow~
    \tuplet 3/2 { des''8 es''8. c''16) }
    \tuplet 3/2 { des''8 ^\upbow bes'8 ^\downbow c''8 ^\upbow }
    \tuplet 3/2 { \slurUp (as'8 ^\downbow bes'8. ges'16) }
    \tuplet 3/2 { as'8 ^\upbow f'8 ^\downbow ges'8 ^\upbow }
  }

  % Mesure 5
  {
    \tuplet 3/2 { \slurUp (f'8 ^\downbow d'8 f'8) }
    \tuplet 3/2 { d'8 ^\upbow \slurUp (f'8 ^\downbow d'8~) }
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
