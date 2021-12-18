class Submarine:

  def __init__(self, commands):
    self.commands = commands
    self.horizontal = 0
    self.depth = 0
    self.aim = 0

  """
  Simulate the provided commands directly on
  the local horizonal and depth variables
  """
  def simulate(self):
    # Loop commands
    for command in self.commands:
      # Split data info direction and amount
      args = command.split(' ')
      direction = args[0]
      amount = int(args[1])

      # Forward movement
      if direction == 'forward':
        self.horizontal += amount
        self.depth += self.aim * amount

      # Down movement
      if direction == 'down':
        self.aim += amount
        # This was only used in the first half
        # self.depth += amount

      # Up movement
      if direction == 'up':
        self.aim -= amount
        # This was only used in the first half
        # self.depth -= amount