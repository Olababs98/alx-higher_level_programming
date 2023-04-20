#!/usr/bin/python3
import sys


def print.solution(solution):
    """print the soln in the required format."""
    for row in solution:
        print("".join(row))

def is.safe(board, row, col, n):
    """chhecks if it is safe to place a queen at board[row[col]."""
    # check row
    for j in range(col):
        if board[row][j] == 'Q':
            return False
    # Check upper diagonal
    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j] == 'Q':
            return False
        i, j = i - 1, j - 1
    # Check lower diagonal
    i, j = row, col
    while i < n and j >= 0:
        if board[i][j] == 'Q':
            return False
        i, j = i + 1, j - 1
    return True

def solve_n_queens(n):
    """Solves the N queens problem."""
    board = [['.' for j in range(n)] for i in range(n)]
    solutions = []
    
    def backtrack(col):
        """Backtracking function to find solutions."""
        nonlocal board
        if col == n:
            solutions.append([row[:] for row in board])
            return
        for row in range(n):
            if is_safe(board, row, col, n):
                board[row][col] = 'Q'
                backtrack(col + 1)
                board[row][col] = '.'
    
    backtrack(0)
    for solution in solutions:
        print_solution(solution)
        print()

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)
    solve_n_queens(n)
