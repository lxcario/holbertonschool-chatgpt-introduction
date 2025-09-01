#!/usr/bin/env python3
import sys

def factorial(n: int) -> int:
    if n < 0:
        raise ValueError("factorial() not defined for negative values")
    result = 1
    while n > 1:
        result *= n
        n -= 1   # Critical fix: progress the loop
    return result

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <non-negative-integer>", file=sys.stderr)
        raise SystemExit(1)
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("Error: argument must be an integer.", file=sys.stderr)
        raise SystemExit(1)
    print(factorial(n))