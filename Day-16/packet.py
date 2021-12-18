from converter import bin_to_int, hexchar_to_int, int_to_bin, pad_array
from functools import reduce
import operator

class Packet:

  def __init__(self, hex=None, bits=None):
    self.packets = []

    # Parse from hex string
    if hex:
      self.hex = hex
      self.parse()
      self.interpret()
    
    # Parse from individual bits
    elif bits:
      self.bits = bits
      self.interpret()
    
    # Error
    else:
      raise ValueError('Please provide either hex or bits!')

  """
  Parse hexadecimal input into quads and bits
  """
  def parse(self):
    # Parse quads of bits for every hex character
    quads = [pad_array(int_to_bin(hexchar_to_int(x)), 4) for x in self.hex]

    # Combine individual quads into single list of bits
    self.bits = [item for quad in quads for item in quad]

  """
  Read bits as a literal value
  """
  def read_literal(self):
    # Loop as long as the bit pointer is still in range
    bitp = 6
    valbits = []
    while len(self.bits) > bitp:
      # Extend by current bits, skip first one (indicator)
      valbits.extend(self.bits[bitp + 1:bitp + 5])

      # First bit is zero, end reached
      if self.bits[bitp] == 0:
        bitp += 5
        break

      # Go to next unit of data
      bitp += 5

    self.literal = bin_to_int(valbits)
    self.end = bitp

  """
  Interpret bits and set as properties
  """
  def interpret(self):
    self.ver = bin_to_int(self.bits[0:3]) # Version
    self.typi = bin_to_int(self.bits[3:6]) # Type ID

    # Literal value
    if self.typi == 4:
      self.read_literal()

    # Packet is of type operator
    else:
      self.lentypi = bin_to_int([self.bits[6]]) # Length type ID
      databegin = 7 + (11 if self.lentypi == 1 else 15) # Begin of inner data
      self.sublen = bin_to_int(self.bits[7:databegin]) # Length of sub-packets

      # Sublist of inner bits remaining
      innerbits = self.bits[databegin:]

      # Keep track of read units of data
      bitsread = 0
      packsread = 0

      # Loop until one exit condition is met
      while (
        (self.lentypi == 0 and bitsread != self.sublen) or
        (self.lentypi == 1 and packsread != self.sublen)
      ):
        p = Packet(bits=innerbits)
        self.packets.append(p)

        # Splice off leading read bits
        innerbits = innerbits[p.end:]

        # Increase counters
        bitsread += p.end
        packsread += 1

      self.end = databegin + bitsread

  """
  Calculate the total sum of all version numbers found
  within this packet and it's subpackets
  """
  def calculate_version_sum(self):
    total = self.ver
    for pack in self.packets:
      total += pack.calculate_version_sum()
    return total

  """
  Execute the operand this packet's type-id specifies
  """
  def execute_operator(self):
    # Literal value
    if self.typi == 4:
      return self.literal

    operands = [packet.execute_operator() for packet in self.packets]

    # Sum
    if self.typi == 0:
      return reduce(operator.add, operands)

    # Product
    if self.typi == 1:
      return reduce(operator.mul, operands)

    # Minimum
    if self.typi == 2:
      return min(operands)

    # Maximum
    if self.typi == 3:
      return max(operands)
    
    # Greater Than
    if self.typi == 5:
      return 1 if operands[0] > operands[1] else 0

    # Less than
    if self.typi == 6:
      return 1 if operands[0] < operands[1] else 0

    # Equal to
    if self.typi == 7:
      return 1 if operands[0] == operands[1] else 0

    raise ValueError(f'Unsupported type id {self.typi}!')