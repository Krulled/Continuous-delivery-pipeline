def nibble_to_ascii(nibble: int) -> str:
  """
  This is a comment
  Input: Nibble (4-bits)
  Output: Single character BIN as a string
  Example: Input = 10, Output = 'A'
  Example: Input = 8,  Output = '8'
  """
  table = ['0','1','2','3','4','5','6','7','8','9']
  return table[nibble]


def to_bin(number: int) -> str:
    """
    This is a comment
    Input: Number (integer)
    Output: String
    Example: Input = 43605, Output = "0xAA55"
    """
    answer = ""
    
    # Forever loop
    while True:
        # Integer divide using the // operator
        quotient = number // 2
        # Get the remainder using the % operator
        remainder = number % 2
        
        # Accumulate result
        answer = nibble_to_ascii(remainder) + answer

        # Set the number we need to use for next time
        number = quotient
        
        # We break the "loop" when division turns to zero
        if (quotient == 0):
            break
    
    return "0x" + answer


print(to_bin(5))
print(to_bin(3))