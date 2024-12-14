def is_valid(board, row, col, num):
    for i in range(9):
        if board[row][i] == num or board[i][col] == num or board[(row // 3) * 3 + i // 3][(col // 3) * 3 + i % 3] == num:
            return False
    return True

def solve_sudoku(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                for num in range(1, 10):
                    if is_valid(board, row, col, num):
                        board[row][col] = num
                        if solve_sudoku(board):
                            return True
                        board[row][col] = 0
                return False
    return True

def print_board(board):
    for row in board:
        print(" ".join(str(num) for num in row))

def input_board():
    board = []
    print("Enter the Sudoku puzzle row by row, with spaces between numbers (use 0 for empty cells):")
    for i in range(9):
        while True:
            try:
                row = list(map(int, input(f"Row {i + 1}: ").split()))
                if len(row) != 9:
                    raise ValueError
                board.append(row)
                break
            except ValueError:
                print("Invalid input. Please enter exactly 9 numbers separated by spaces.")
    return board

if __name__ == "__main__":
    # User inputs the Sudoku board
    sudoku_board = input_board()

    if solve_sudoku(sudoku_board):
        print("Solved Sudoku board:")
        print_board(sudoku_board)
    else:
        print("No solution exists")
