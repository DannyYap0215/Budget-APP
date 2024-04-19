import tkinter as tk
import set_income
import set_categories

def open_set_income_window():
    set_income.open_set_income_window()
    
def open_set_categories_window():
    set_categories.open_set_categories_window()

def open_edit_budget_window():
    
    edit_budget_window = tk.Toplevel()
    edit_budget_window.title("Edit Budget")
    edit_budget_window.geometry("400x300")

    set_income_button = tk.Button(edit_budget_window, text="Set Income",command=open_set_income_window)
    set_income_button.grid(row=0, column=0, padx=10, pady=5, sticky="w")
    
    set_categories_button = tk.Button(edit_budget_window, text="Set Categories",command=open_set_categories_window)
    set_categories_button.grid(row=1, column=0, padx=10, pady=5, sticky="w")
    


