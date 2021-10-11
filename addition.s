addition:
  ; Begin by pulling return address off of stack.
  PLA
  STA $00
  PLA
  STA $01

  ; Pull 2 LSBs of second parameter off of stack.
  PLA
  STA $02
  PLA
  STA $03

  ; Pull MSB of mantissa off of stack and shift exponent LSB into carry.
  PLA
  ASL
  STA $04

  ; Pull MSB off of stack, shift in exponent LSB, store sign at $06.
  PLA
  ROL
  STA $05
  ROL $06

  ; Pull 2 LSBs of first parameter off of stack.
  PLA
  STA $07
  PLA
  STA $08

  ; Pull MSB of mantissa off of stack and shift exponent LSB into carry.
  PLA
  ASL
  STA $09

  ; Pull MSB off of stack, shift in exponent LSB, store sign at $0b.
  PLA
  ROL
  STA $0a
  ROL $0b

  ; Add appropriate implicit 1's/0's to mantissas.
  ; Shift in an implicit 1 if exponent != 0, else implicit 0.
.add_second_implicit_bit:
  LDA $05
  CMP #$00
  BNE .second_parameter_normal
  CLC
  ROR $04
  JMP .add_first_implicit_bit
.second_parameter_normal:
  SEC
  ROR $04
  
.add_first_implicit_bit:
  LDA $0a
  CMP #$00
  BNE .first_parameter_normal
  CLC
  ROR $09
  JMP .align_mantissas
.first_parameter_normal:
  SEC
  ROR $09

.align_mantissas:
  ; Y stores the number of 1 bits shifted off in alignment.
  ; Carry bit stores the value of the last bit shifted off.
  LDY #$00
  CLC
  PHP

  ; Subtract EXP2 from EXP1 already stored in A.
  ; If EXP1 - EXP2 == 0, sum mantissas.
  ; If EXP1 - EXP2  > 0, shift second mantissa down.
  ; If EXP1 - EXP2  < 0, shift first mantissa down.
  SEC
  SBC $05
  BEQ .sum_mantissas
  TAX
  BPL .shift_second_mantissa

.shift_first_mantissa:
  ; Remove old carry bit from stack.
  ; Rotate first mantissa right by 1 bit.
  ; Push new carry bit onto stack.
  ; If a 1 was shifted off, increment Y.
  ; Increment X, if X == 0, proceed to sum mantissas.
  PLP
  LSR $09
  ROR $08
  ROR $07
  PHP
  BCC .zero_shifted_out_first
  INY
.zero_shifted_out_first:
  INX
  CPX #$00
  BNE .shift_first_mantissa
  
  ; We operate in place on the first parameter, so update its exponent.
  LDA $05
  STA $0a
  JMP .sum_mantissas

.shift_second_mantissa:
  ; Remove old carry bit from stack.
  ; Rotate second mantissa right by 1 bit.
  ; Push new carry bit onto stack.
  ; If a 1 was shifted off, increment Y.
  ; Decrement X, if X == 0, proceed to sum mantissas.
  PLP
  LSR $04
  ROR $03
  ROR $02
  PHP
  BCC .zero_shifted_out_second
  INY
.zero_shifted_out_second:
  DEX
  CPX #$00
  BNE .shift_second_mantissa

.sum_mantissas:
  ; Add second mantissa to first mantissa.
  ; If addition overflows, shift mantissa down and increment exponent.
  CLC
  LDA $07
  ADC $02
  STA $07
  LDA $08
  ADC $03
  STA $08
  LDA $09
  ADC $04
  STA $09
  BCC .round
  ROR $09
  ROR $08
  ROR $07
  INC $0a

.round:
  ; Round new mantissa to even.
  ; If bits shifted off had pattern 0xxx, simply truncate and return.
  ; If bits shifted off had pattern 1xxx with Y >= 2, increment mantissa.
  ; Otherwise, increment mantissa if LSB is 1.
  PLP
  BCC .return

.rounding_msb_one:
  CPY #$02
  BCS .increment_mantissa

  LDA $09
  AND #$01
  BEQ .return

.increment_mantissa:
  ; Increment the mantissa by 1.
  ; If shifting overflows the mantissa, shift mantissa down and round again.
  CLC
  LDA $07
  ADC #$01
  STA $07
  LDA $08
  ADC #$00
  STA $08
  LDA $09
  ADC #$00
  STA $09
  BCC .return

  ROR $09
  ROR $08
  ROR $07
  PHP
  INC $0a
  PLP
  BCC .return
  INY
  JMP .rounding_msb_one

.return:
  ; Shift out implicit bit, shift exponent and sign through.
  ; Push return value onto stack.
  ; Push return address onto stack.
  ; Return from subroutine.
  ASL $09
  LSR $0b
  ROR $0a
  ROR $09

  LDA $0a
  PHA
  LDA $09
  PHA
  LDA $08
  PHA
  LDA $07
  PHA

  LDA $01
  PHA
  LDA $00
  PHA

  RTS
