from packet import Packet

"""
Entrypoint of this program
"""
def main():
  with open('input.txt', 'r') as inp:
    # Decode packets with one packet per line, strip line contents
    for line in list(map(lambda x: x.strip(), inp.readlines())):

      # Skip empty lines or comments
      if line == '' or line.startswith('#'):
        continue
      
      # Parse line
      p = Packet(hex=line)

      # Then print it's HEX value, it's version sum and it's operation result
      print(f'{line} -> V{p.calculate_version_sum()}, result={p.execute_operator()}')

if __name__ == '__main__':
  main()