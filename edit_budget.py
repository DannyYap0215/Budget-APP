import tkinter as tk

categories = ["apple", "banana", "melon"]

def open_edit_budget_window():
    global category_menu
    def save_budget():      #tk._setit() means set selected_category_var to be add_categories_entry.get() #this is needed so the value entered can be choosen from the dropdown menu
        category_menu['menu'].add_command(label=add_categories_entry.get(), command=tk._setit(selected_category_var, add_categories_entry.get()))

    edit_budget_window = tk.Toplevel()
    edit_budget_window.title("Edit Budget")
    edit_budget_window.geometry("600x600")

    #income //no features for now
    income_label = tk.Label(edit_budget_window, text="Income:")
    income_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")
    income_entry = tk.Entry(edit_budget_window)
    income_entry.grid(row=0, column=1, padx=10, pady=5)

    #month issued //no features for now
    month_issued_label = tk.Label(edit_budget_window, text="Month Issued:")
    month_issued_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")
    month_issued_entry = tk.Entry(edit_budget_window)
    month_issued_entry.grid(row=1, column=1, padx=10, pady=5)

    #add categories
    add_categories_label = tk.Label(edit_budget_window, text="Add Categories:")
    add_categories_label.grid(row=2, column=0, padx=10, pady=5, sticky="w")
    add_categories_entry = tk.Entry(edit_budget_window)
    add_categories_entry.grid(row=2, column=1, padx=10, pady=5)

    # select categories
    select_categories_label = tk.Label(edit_budget_window, text="Select Categories:")
    select_categories_label.grid(row=3, column=0, padx=10, pady=5, sticky="w")
    selected_category_var = tk.StringVar(edit_budget_window)
    category_menu = tk.OptionMenu(edit_budget_window, selected_category_var, *categories)
    category_menu.grid(row=3, column=1, padx=10, pady=5)

    save_button = tk.Button(edit_budget_window, text="Save", command=save_budget)
    save_button.grid(row=4, column=1)

