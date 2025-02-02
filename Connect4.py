import easygui as e
import tkinter as tk
from tkinter import messagebox

class Connect4Game:
    def __init__(self, master):
        self.master = master
        self.master.title('Connect 4')
        self.master.configure(bg='#3498db')
        self.board =  [[0] * 7 for _ in range(6)]
        self.turn = 1
        self.create_drop_button(0)
        self.create_widgets() 


    def create_widgets(self):
        self.buttons = []
        for row in range(6):
            button_row = []
            for col in range(7):
                button = tk.Button(self.master, text="", width=5, height=2, bg="#95a5a6", 
                                   font=("Helvetica", 12, "bold"), 
                                   command=lambda r=row, c=col: self.drop_piece(r, c), 
                                   relief="ridge", bd=4)
                button.grid(row=row, column=col, padx=5, pady=5)
                button_row.append(button)
            self.buttons.append(button_row)

    def create_drop_button(self, col):
        self.buttons = []
        for row in range(6):
            button_row = []
            for col in range(7):
                button = tk.Button(self.master, text=f"Drop", width=4, height=1, bg="white", 
                                font=("Helvetica", 12, "bold"), 
                                command=lambda c=col: self.drop_piece(0, c), 
                                relief="raised", bd=4)
                button.grid(row=row+1, column=col, padx=5, pady=5)
                button_row.append(button)
            self.buttons.append(button_row)
        return button

    def drop_piece(self, row, col):
        if self.board[row][col] == 0:
            current_row = row
            while current_row < 5 and self.board[current_row+1][col] == 0:
                current_row += 1
            self.board[current_row][col] = self.turn
            self.update_drop_peices(current_row, col)
            if self.check_winner(current_row, col):
                messagebox.showinfo("Winner", f"Player {self.turn} wins!")
                self.reset_board()
            elif all(self.board[r][c] != 0 for r in range(6) for c in range(7)):
                messagebox.showinfo("Draw", "It's a draw!")
                self.reset_board()
            else:
                self.turn = 3 - self.turn
    

    def update_drop_peices(self, row, col):
        player = self.board[row][col]
        color = "red" if player == 1 else "yellow"
        self.buttons[row][col].config(bg=color, state="disabled")

    def check_winner(self, row, col):
        directions = [(1, 0), (0, 1), (1, 1), (-1, 1)]
        for dr, dc in directions:
            count = 1
            for direction in [1, -1]:
                r, c = row + dr * direction, col + dc * direction
                while 0 <= r < 6 and 0 <= c < 7 and self.board[r][c] == self.turn:
                    count += 1
                    r += dr * direction
                    c += dc * direction
            if count >= 4:
                return True
        return False

    def reset_board(self):
        for row in range(6):
            for col in range(7):
                self.board[row][col] = 0
                self.buttons[row][col].config(text="", bg="#95a5a6", state="normal")
        self.turn = 1


if __name__ == '__main__':
    root = tk.Tk()
    game = Connect4Game(root)
    root.mainloop()