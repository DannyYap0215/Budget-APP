import tkinter as tk
import customtkinter as ctk
from customtkinter import *
import edit_budget

root = tk.Tk()
root.title("Tkinter Sample")
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.geometry(f"{screen_width}x{screen_height}")

def toggle_fullscreen(event=None):
    state = not root.attributes('-fullscreen') #True or False basically 
    root.attributes('-fullscreen', state)
    
def open_edit_budget_window():
    edit_budget.open_edit_budget_window()

insight_button = tk.Button(root, text="Insight", command=toggle_fullscreen)
insight_button.grid(row=0, column=1, padx=10, pady=5, sticky="w")

edit_budget_button = tk.Button(root, text="Edit Budget", command=open_edit_budget_window)
edit_budget_button.grid(row=1, column=1, padx=10, pady=5,sticky="w")

update_expenses_button = tk.Button(root, text="Update Expenses", command=toggle_fullscreen)
update_expenses_button.grid(row=2, column=1, padx=10, pady=5, sticky="w")


root.bind("<F11>", toggle_fullscreen)

root.mainloop()
