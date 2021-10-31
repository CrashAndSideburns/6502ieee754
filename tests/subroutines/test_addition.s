  .org ORIGIN
test_addition:
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

  JSR addition

  PLA
  STA ADDRIO
  PLA
  STA ADDRIO
  PLA
  STA ADDRIO
  PLA
  STA ADDRIO

  BRK

  .include "../../addition.s"
