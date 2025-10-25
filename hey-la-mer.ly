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
  % En avant la musique !
  b16 c8. g'2. g2.  r4 
  \relative c' {
  b16 c8 g'2. b8 c8.
  }
  \relative c' {
  g'16 b8 f8 g8 d8 e8. b16 c8 a8. c16 e8 c8 e8 g8 e8. g16 a8 g8 a8 g8 a8. g16 a8 
g8. a16 g8 a8 g8  }
  \relative c' \clef treble {
    bes8 ges8. bes16 des4 des8 ees8. c16 des8 bes8 c8 aes8 bes8. ges16 aes8 f8 ges8  
  }
  \relative c' {
  f d f d f d d
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
