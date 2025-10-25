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

violin = \relative c' {
  \global

  % Mesure 1
  \slurUp (b16 ^\upbow c8.)
  \slurUp (g'2 ^\downbow. g2.) r4

  % Mesure 2
  \relative c' {
    \slurUp (b16 ^\upbow c8.)
    g'2 ^\downbow
    \tuplet 3/2 { \slurUp (b8 ^\upbow c8. g16) }
  }

  % Mesure 3
  \relative c' {
    \tuplet 3/2 { b8 ^\downbow' f8 ^\upbow g8 ^\downbow }
    \tuplet 3/2 { d8 ^\upbow e8 ^\downbow b8 ^\upbow }
    c4 ^\downbow~ 
    \tuplet 3/2 { c8 ^\upbow \slurUp (a8 ^\downbow c8 }
    \tuplet 3/2 { e8) \slurUp (c8 ^\upbow e8 }
    \tuplet 3/2 { g8) \slurUp (e8 ^\downbow g8) }
    \tuplet 3/2 { a8 ^\upbow. g16 ^\downbow \slurUp (a8 ^\upbow }
    \tuplet 3/2 { g8) \slurUp (a8 ^\downbow g8) }
    \tuplet 3/2 { a8 ^\upbow. g16 ^\downbow \slurUp (a8 ^\upbow }
    \tuplet 3/2 { g8) \slurUp (a8 ^\downbow g8) }
  }

  % Mesure 4 — clef treble
  \relative c' \clef treble {
    \tuplet 3/2 { \slurUp (bes8 ^\upbow ges8. bes16) }
    \slurUp (des4 ^\downbow~
    \tuplet 3/2 { des8 ees8. c16) }
    \tuplet 3/2 { des8 ^\upbow bes8 ^\downbow c8 ^\upbow }
    \tuplet 3/2 { \slurUp (aes8 ^\downbow bes8. ges16) }
    \tuplet 3/2 { aes8 ^\upbow f8 ^\downbow ges8 ^\upbow }
  }

  % Mesure 5
  \relative c' {
    \tuplet 3/2 { \slurUp (f8 ^\downbow d8 f8) }
    \tuplet 3/2 { d8 ^\upbow \slurUp (f8 ^\downbow d8~) }
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
