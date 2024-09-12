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
        self.create_drop_widgets(0)
        self.create_widgets() 


    def create_widgets(self):
        pass

    def create_drop_widgets(self, col):
        pass

    def drop_piece(self, col, row):
        pass

    def update_drop_peices(self, col, row):
        pass

    def check_winner(self, col, row):
        pass

    def reset_board(self):
        pass


if __name__ == '__main__':
    root = tk.Tk()
    game = Connect4Game(root)
    root.mainloop()