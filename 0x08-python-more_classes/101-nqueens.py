#!/usr/bin/python3
import sys


def n_queens(N):
    if not isinstance(N, int):
        print("N must be a number")
        sys.exit(1)
    elif N < 4:
        print("N must be at least 4")
        sys.exit(1)

    queens = []
    solve(queens, N)


def solve(queens, N):
    if len(queens) == N:
        print(queens)
        return
    for i in range(N):
        if is_valid(queens, i):
            queens.append(i)
            solve(queens, N)
            queens.pop()


def is_valid(queens, col):
    row = len(queens)
    for i, q in enumerate(queens):
        if q == col or abs(q - col) == row - i:
            return False
    return True


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    n_queens(N)
