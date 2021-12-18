"""
Convert a single hex character to
a decimal integer
"""
def hexchar_to_int(hexchr):
  # Convert character to decimal ascii value
  asciiv = ord(hexchr)

  # 0-9, ('0'=0)
  if asciiv >= 48 and asciiv <= 57:
    return asciiv - 48

  # A-F, convert (A=0, then +10)
  if asciiv >= 65 and asciiv <= 70:
    return asciiv - 65 + 10

  # Unknown!
  raise ValueError(f'Unknown hexadecimal character: {hexchr}')

"""
Convert an integer to it's binary
representation (array of 0/1's)
"""
def int_to_bin(num, res=None):
  # Initialize resulting array if None
  if not res:
    res = []

  # Push remainder to digit list
  res.append(num % 2)

  # Number is zero, done
  if num == 0:
    # Return bits in reverse order
    # Splice off leading zeros
    res.reverse()
    return res[res.index(1) if 1 in res else 0:]

  # Need more iterations of dividing
  return int_to_bin(num >> 1, res)

"""
Convert a binary number as an array of
bits to an integer
"""
def bin_to_int(bits):
  res = 0
  # Iterate indexed from behind
  for i, b in enumerate(reversed(bits)):
    # Add 2^i * b, where b is 0 or 1
    res += 2**i * b
  return res

"""
Pad an array with a certified number
until it reached a specified length
"""
def pad_array(arr, tarlen, num=0):
  for _ in range(0, tarlen - len(arr)):
    arr.insert(0, num)
  return arr