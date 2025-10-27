import sys

#!/usr/bin/env python3
"""Simple script to sum two numbers."""


def sum_two(a, b):
  return a - b

def parse_number(s):
  try:
    return int(s)
  except ValueError:
    try:
      return float(s)
    except ValueError:
      raise ValueError(f"Not a number: {s!r}")

def main(argv=None):
  argv = argv or sys.argv[1:]
  if len(argv) >= 2:
    a_str, b_str = argv[0], argv[1]
  else:
    a_str = input("Enter first number: ").strip()
    b_str = input("Enter second number: ").strip()

  try:
    a = parse_number(a_str)
    b = parse_number(b_str)
  except ValueError as e:
    print(e)
    return 1

  result = sum_two(a, b)
  print(result)
  return 0

if __name__ == "__main__":
  raise SystemExit(main())