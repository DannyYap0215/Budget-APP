from customtkinter import *
import edit_budget
import update_expenses
import expenses_history
import expenses_piechart
import income_piechart
import insight


root = CTk()
root.title("Budget!")
screen_width = 500
screen_height = 300
root.geometry(f"{screen_width}x{screen_height}")

set_appearance_mode("dark")

def toggle_fullscreen(event=None):
    state = not root.attributes('-fullscreen') #True or False basically 
    root.attributes('-fullscreen', state)
    
def open_edit_budget_window():
    edit_budget.open_edit_budget_window()
    
def open_update_expenses_window():
    update_expenses.open_update_expenses_window()

def open_insight_window():
    insight.open_insight_window(expenses_piechart, income_piechart)

def open_expenses_history_window():
    expenses_history.open_expenses_history_window()
    
insight_button = CTkButton(root, text="Insight", height= 10,width=20, command=open_insight_window)
insight_button.grid(row=0, column=1, padx=10, pady=5, sticky="w",)

edit_budget_button = CTkButton(root, text="Edit Budget", height= 10,width=20, command=open_edit_budget_window)
edit_budget_button.grid(row=1, column=1, padx=10, pady=5,sticky="w")

update_expenses_button = CTkButton(root, text="Update Expenses",height= 10,width=20, command=open_update_expenses_window)
update_expenses_button.grid(row=2, column=1, padx=10, pady=5, sticky="w")

expenses_history_button = CTkButton(root, text="Expenses History",height= 10,width=20, command=open_expenses_history_window)
expenses_history_button.grid(row=3, column=1, padx=10, pady=5, sticky="w")

root.bind("<F11>", toggle_fullscreen)

root.mainloop()
