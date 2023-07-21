import tkinter as tk
import customtkinter as ctk

class Table:
    def __init__(self, root, columns):
        self.root = root
        self.columns = columns

        self.draw_header()

    def get_width(self, i):
        if i == 0:
            return 50
        elif i == 1:
            return 250
        elif i == 2:
            return 400
        elif i == 3:
            return 100
        elif i == 4:
            return 100
        else:
            return 20
    
    def draw_header(self):
        for i, column in enumerate(self.columns):
            width = self.get_width(i)
            ctk.CTkLabel(self.root, text=column, width=width, anchor="w").grid(row=0, column=i, padx=5, pady=5)

    def add_data(self, data):
        for i, row in enumerate(data):
            for j, cell in enumerate(row):
                width = self.get_width(j)
                label1 = ctk.CTkEntry(self.root, width=width)
                label1.insert(0, cell)
                label1.configure(state="readonly")
                label1.grid(row=i+1, column=j, padx=5, pady=5)

    def delete_data(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        self.draw_header()