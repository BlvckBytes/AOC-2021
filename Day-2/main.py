"""
Entrypoint of this program
"""
from submarine import Submarine


def main():
  with open('input.txt', 'r') as f:

    commands = []

    # Read file line by line, trim lines
    for line in list(map(lambda x: x.strip(), f.readlines())):

      # Skip empty or commented lines
      if line == '' or line.startswith('#'):
        continue
      
      # Exit keyword stops file processing
      if line == 'exit':
        break
      
      # Add command to list
      commands.append(line)

    # Create submarine and simulate
    sm = Submarine(commands)
    sm.simulate()

    print(f'Horizontal: {sm.horizontal}, Depth: {sm.depth}, Result: {sm.horizontal * sm.depth}')

if __name__ == '__main__':
  main()