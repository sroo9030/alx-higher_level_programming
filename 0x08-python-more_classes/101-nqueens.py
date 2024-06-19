#!/usr/bin/python3
# 101-nqueens.py

import sys


def is_safe(board, row, col, n):
    """Check if it's safe to place a queen at the given
    position (row, col) on the board.

    """
    # Check if there is a queen in the same row to the left
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on the left
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on the left
    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def solve_nqueens_util(board, col, n, solutions):
    """
    Recursively find all solutions to the N-Queens problem.
    """
    if col == n:
        # If all queens are placed, add the solution to the list
        solutions.append([[i, board[i].index(1)] for i in range(n)])
        return

    for i in range(n):
        if is_safe(board, i, col, n):
            board[i][col] = 1
            solve_nqueens_util(board, col + 1, n, solutions)
            board[i][col] = 0  # Backtrack


def solve_nqueens(n):
    """
    Initialize the board and start solving the N-Queens problem.
    """
    board = [[0] * n for _ in range(n)]
    solutions = []
    solve_nqueens_util(board, 0, n, solutions)

    # Print each solution
    for solution in solutions:
        print(solution)
    print()


def main():
    """
    Parse command line arguments and execute the N-Queens solver.
    """
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

    solve_nqueens(n)


if __name__ == "__main__":
    main()
