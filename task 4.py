import tkinter as tk
from tkinter import ttk, messagebox
import random

class SudokuSolver:
    def __init__(self, root):
        self.root = root
        self.root.title("Sudoku Solver")

        self.board = [[0 for _ in range(9)] for _ in range(9)]

        self.entries = [[None for _ in range(9)] for _ in range(9)]
        for row in range(9):
            for col in range(9):
                self.entries[row][col] = ttk.Entry(root, width=2, font=('Arial', 18), justify='center')
                self.entries[row][col].grid(row=row, column=col, padx=5, pady=5)

        self.solve_button = ttk.Button(root, text="Solve", command=self.solve_sudoku)
        self.solve_button.grid(row=9, column=4, pady=10)

    def is_valid(self, board, row, col, num):
        for i in range(9):
            if board[row][i] == num or board[i][col] == num or board[(row // 3) * 3 + i // 3][(col // 3) * 3 + i % 3] == num:
                return False
        return True

    def solve_sudoku(self):
        for row in range(9):
            for col in range(9):
                value = self.entries[row][col].get()
                self.board[row][col] = int(value) if value else 0

        if self.solve_board():
            self.display_board()
            messagebox.showinfo("Success", "Sudoku solved!")
        else:
            messagebox.showerror("Error", "No solution exists for the given Sudoku puzzle.")

    def solve_board(self):
        for row in range(9):
            for col in range(9):
                if self.board[row][col] == 0:
                    for num in range(1, 10):
                        if self.is_valid(self.board, row, col, num):
                            self.board[row][col] = num
                            if self.solve_board():
                                return True
                            self.board[row][col] = 0
                    return False
        return True

    def display_board(self):
        for row in range(9):
            for col in range(9):
                self.entries[row][col].delete(0, tk.END)
                self.entries[row][col].insert(0, str(self.board[row][col]))

# Create the main window
root = tk.Tk()
sudoku_solver = SudokuSolver(root)

# Run the application
root.mainloop()
