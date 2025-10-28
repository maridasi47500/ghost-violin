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
  \slurUp (bes16 c8.)
  \slurUp (g'2. g2.) r4
  }
  % Mesure 2
  \relative c' {
    \slurUp (bes16 c8.)
    g'2
    \tuplet 3/2 { \slurUp (bes8 c8. g16) }
  }

  % Mesure 3
  \relative c'' {
    \tuplet 3/2 { bes8 f8 g8 }
    \tuplet 3/2 { d8 ees8. bes16 }
    c4~ 
    \tuplet 3/2 { c8 \slurUp (a8 c8 }
    \tuplet 3/2 { ees8) \slurUp (c8. ees16 }
    \tuplet 3/2 { g8) \slurUp (ees8 g8) }
    \tuplet 3/2 { a8 g8. \slurUp (a16 }
    \tuplet 3/2 { g8) \slurUp (a8 g8) }
    \tuplet 3/2 { a8 g8. \slurUp (a16 }
    \tuplet 3/2 { g8) \slurUp (a8 g8) }
  }

  % Mesure 4 — clef treble
  \relative c''  {
    \tuplet 3/2 { \slurUp (bes8 ges8. bes16) }
    \slurUp (des4~
    \tuplet 3/2 { des8 ees8. c16) }
    \tuplet 3/2 { des8 bes8 c8 }
    \tuplet 3/2 { \slurUp (aes8 bes8. ges16) }
    \tuplet 3/2 { aes8 f8 ges8 }
  }

  % Mesure 5
  \relative c' {
    \tuplet 3/2 { \slurUp (f8 d8. f16) }
    \tuplet 3/2 { d8 \slurUp (f8 d8~) }
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
