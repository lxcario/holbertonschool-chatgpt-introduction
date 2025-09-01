#!/usr/bin/env python3
import sys

def factorial(n: int) -> int:
    """Return n! for non-negative integer n."""
    if n < 0:
        raise ValueError("factorial() not defined for negative values")
    result = 1
    while n > 1:
        result *= n
        n -= 1          # Decrement n so the loop progresses
    return result

def main(argv):
    if len(argv) != 2:
        print(f"Usage: {argv[0]} <non-negative-integer>", file=sys.stderr)
        return 1
    try:
        n = int(argv[1])
    except ValueError:
        print("Error: argument must be an integer.", file=sys.stderr)
        return 1
    try:
        print(factorial(n))
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1
    return 0

if __name__ == "__main__":
    raise SystemExit(main(sys.argv))