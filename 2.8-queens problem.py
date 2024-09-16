def print_board(board):
    for row in board:
        print(" ".join(row))
    print()

def is_safe(board, row, col):
    for i in range(col):
        if board[row][i] == 'Q':
            return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 'Q':
            return False

    for i, j in zip(range(row, len(board)), range(col, -1, -1)):
        if board[i][j] == 'Q':
            return False

    return True

def solve_n_queens(board, col):
    if col >= len(board):
        return True

    for i in range(len(board)):
        if is_safe(board, i, col):
            board[i][col] = 'Q'

            if solve_n_queens(board, col + 1):
                return True

            board[i][col] = '.'  # Backtrack

    return False

def solve():
    N = 8
    board = [['.' for _ in range(N)] for _ in range(N)]

    if solve_n_queens(board, 0):
        print_board(board)
    else:
        print("Solution does not exist")

solve()
