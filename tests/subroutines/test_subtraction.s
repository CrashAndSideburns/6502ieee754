  .org ORIGIN
test_subtraction:
  LDA ADDRIO
  PHA
  LDA ADDRIO
  PHA
  LDA ADDRIO
  PHA
  LDA ADDRIO
  PHA
  LDA ADDRIO
  PHA
  LDA ADDRIO
  PHA
  LDA ADDRIO
  PHA
  LDA ADDRIO
  PHA

  JSR subtraction

  PLA
  STA ADDRIO
  PLA
  STA ADDRIO
  PLA
  STA ADDRIO
  PLA
  STA ADDRIO

  BRK

  .include "../../arithmetic/subtraction.s"
