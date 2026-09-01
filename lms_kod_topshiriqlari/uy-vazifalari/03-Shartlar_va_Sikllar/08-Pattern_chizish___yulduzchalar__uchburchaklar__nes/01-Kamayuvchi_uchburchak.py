import sys


def solve():
  input_data = sys.stdin.read().split()
  if not input_data:
    return

  n = int(input_data[0])
    
  for i in range(n, 0, -1):
    print("*" * i)


if __name__ == "__main__":
  solve()