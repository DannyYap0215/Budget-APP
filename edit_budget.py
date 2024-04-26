from customtkinter import *
import set_income
import set_categories

def open_set_income_window():
    set_income.open_set_income_window()
    
def open_set_categories_window():
    set_categories.open_set_categories_window()
    
def open_edit_budget_window():
    
    def on_button_click():
        # Reduce the topmost attribute when a button is clicked
        edit_budget_window.wm_attributes("-topmost", False)
    
    edit_budget_window = CTkToplevel()
    edit_budget_window.title("Edit Budget")
    edit_budget_window.geometry("400x300")
    edit_budget_window.wm_attributes("-topmost",True)

    set_income_button = CTkButton(edit_budget_window, text="Set Income",command=open_set_income_window)
    set_income_button.grid(row=0, column=0, padx=10, pady=5, sticky="w")
    
    set_categories_button = CTkButton(edit_budget_window, text="Set Categories",command=open_set_categories_window)
    set_categories_button.grid(row=1, column=0, padx=10, pady=5, sticky="w")
    
    #check for m1 click on the button if so it goes through the function o_b_c()
    set_income_button.bind("<Button-1>", lambda event: on_button_click())
    set_categories_button.bind("<Button-1>", lambda event: on_button_click())


