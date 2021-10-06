addition:
pop_return_address:
  ; Begin by pulling return address off of stack.
  PLA
  STA $00
  PLA
  STA $01

pop_second_parameter:
  ; Pull 2 LSBs of second parameter off of stack.
  PLA
  STA $02
  PLA
  STA $03

  ; Pull MSB of mantissa off of stack and shift exponent LSB into carry.
  PLA
  ASL
  STA $04

  ; Pull MSB off of stack, shift in exponent LSB, store sign in byte 5.
  PLA
  ROL
  STA $05
  ROL $06

pop_first_parameter:
  ; Pull 2 LSBs of first parameter off of stack.
  PLA
  STA $07
  PLA
  STA $08

  ; Pull MSB of mantissa off of stack and shift exponent LSB into carry.
  PLA
  ASL
  STA $09

  ; Pull MSB off of stack, shift in exponent LSB, store sign in byte 5.
  PLA
  ROL
  STA $0a
  ROL $0b

  ; Add appropriate implicit 1's/0's to mantissas.
add_second_implicit_bit:
  ; Shift in an implicit 1 if exponent != 0, else implicit 0.
  LDA $05
  CMP #$00
  BEQ second_parameter_subnormal
  SEC
  ROR $04
  JMP add_first_implicit_bit
second_parameter_subnormal:
  CLC
  ROR $04
add_first_implicit_bit:
  ; Shift in an implicit 1 if exponent != 0, else implicit 0.
  LDA $0a
  CMP #$00
  BEQ first_parameter_subnormal
  SEC
  ROR $09
  JMP align_mantissas
first_parameter_subnormal:
  CLC
  ROR $09

align_mantissas:
  LDY #$00
  SEC
  SBC $05 ; Accumulator now contains exp1 - exp2.
  BEQ sum_mantissas
  TAX     ; Store difference in X register.
  BPL shift_second_mantissa ; Shift second mantissa if exp1 > exp2.
shift_first_mantissa:
  ; rotate all bits of mantissa one right
  LSR $09
  ROR $08
  ROR $07
  ; increment Y if the bit shifted out was a 1
  BCC zero_shifted_out_first
  INY
zero_shifted_out_first:
  ; increment X. loop if X != 0, otherwise proceed to sum mantissas
  INX
  CPX #$00
  BNE shift_first_mantissa
  ; first float must have correct exponent
  LDA $05
  STA $0a
  JMP sum_mantissas

shift_second_mantissa:
  ; rotate all bits of mantissa one right
  LSR $04
  ROR $03
  ROR $02
  ; increment Y if the bit shifted out was a 1
  BCC zero_shifted_out_second
  INY
zero_shifted_out_second:
  ; decrement X. loop if X != 0
  DEX
  CPX #$00
  BNE shift_second_mantissa

sum_mantissas:
  CLC
  ; sum mantissas
  LDA $07
  ADC $02
  STA $07
  LDA $08
  ADC $03
  STA $08
  LDA $09
  ADC $04
  STA $09
  ; if mantissas do not overflow, return
  BCC return
  ; if mantissa overflows, shift mantissa down and increment exponent
  ROR $09
  ROR $08
  ROR $07
  INC $0a

return:
  ; shift implied bit out of mantissa, rotate sign and exp LSB through
  ASL $09
  LSR $0b
  ROR $0a
  ROR $09

  ; push return value onto stack
  LDA $0a
  PHA
  LDA $09
  PHA
  LDA $08
  PHA
  LDA $07
  PHA

  ; push return address back onto stack
  LDA $01
  PHA
  LDA $00
  PHA

  RTS
