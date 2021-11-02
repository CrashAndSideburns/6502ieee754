subtraction:
  ; Pull MSB of second parameter off of stack, flip sign bit, and push back to stack.
  ; Proceed to addition.
  TSX
  TXA
  CLC
  ADC #$05
  TAX
  TXS
  PLA
  EOR #$80
  PHA
  TXA
  SEC
  SBC #$05
  TAX
  TXS

  .include "addition.s"