"""
Entrypoint of this program
"""
def main():
  with open('input.txt', 'r') as f:
    measurements = []
    increases = 0

    # Read file line by line, trim lines
    for line in list(map(lambda x: x.strip(), f.readlines())):

      # Skip empty or commented lines
      if line == '' or line.startswith('#'):
        continue
      
      # Exit keyword stops file processing
      if line == 'exit':
        break
      
      # Add measurement as integer
      measurements.append(int(line))

      # Get current and previous elements
      mlen = len(measurements)
      curr = measurements[mlen - 1]
      prev = measurements[mlen - 2] if mlen > 1 else None

      # Print number without newline
      print(curr, ' ', sep='', end='')

      # First element
      if prev == None:
        print('(N/A - no previous measurement)')

      # Current bigger than previous
      elif curr > prev:
        increases += 1
        print('(increased)')

      # Current smaller than previous
      else:
        print('(decreased)')

    # Print statistics
    print(f'> There were {increases} number-increases!')

    last = None # Last sum
    sumincr = 0
    for i in range(0, len(measurements) - 2):
      # Create sum-window of length 3
      a = sum(measurements[i:i+3])

      # No last datapoint, set and skip current
      if last == None:
        last = a
        continue
      
      # Compare and count
      if a > last:
        sumincr += 1
      last = a

    # Print statistics
    print(f'There were {sumincr} sum-increases!')

if __name__ == '__main__':
  main()