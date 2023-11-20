

def is_safe(board, row, col, n):
    # Check if there is a queen in the same column
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check upper diagonal on right side
    for i, j in zip(range(row, -1, -1), range(col, n)):
        if board[i][j] == 1:
            return False

    return True

def print_board(board):
    for row in board:
        print(' '.join(['Q' if x == 1 else '.' for x in row]))

def solve_n_queens_util(board, row, n):
    if row == n:
        # All queens are placed, print the board
        print_board(board)
        print("\n")
        return

    for col in range(n):
        if is_safe(board, row, col, n):
            # Place queen
            board[row][col] = 1

            # Recur to place rest of the queens
            solve_n_queens_util(board, row + 1, n)

            # Backtrack if placing queen in the current position doesn't lead to a solution
            board[row][col] = 0

def solve_n_queens(n, initial_queen_col):
    # Create an empty chessboard
    board = [[0] * n for _ in range(n)]

    # Place the first queen in the specified column
    board[0][initial_queen_col] = 1

    # Start solving from the next row
    solve_n_queens_util(board, 1, n)

# Example usage:
n = 4  # Change this to the desired board size
initial_queen_col = 1  # Change this to the desired column for the first queen
solve_n_queens(n, initial_queen_col)
