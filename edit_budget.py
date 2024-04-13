import tkinter as tk

categories = [
    "Rent",
    "Utility",
    "Food"
]

months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

def open_edit_budget_window():
    global categories
    
    def save_budget():
        new_category = add_categories_entry.get()
        if new_category not in categories and new_category != "":
            categories.append(new_category) #set the entry text as Var, so it can be added as a menu 
            category_menu['menu'].add_command(command=tk._setit(selected_category_var, add_categories_entry.get()), label=add_categories_entry.get())
            add_categories_entry.delete(0, 'end') #deletes from the first index to the end of the widget entry 
        else:
            pass

    edit_budget_window = tk.Toplevel()
    edit_budget_window.title("Edit Budget")
    edit_budget_window.geometry("400x300")

    income_label = tk.Label(edit_budget_window, text="Income:")
    income_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")
    income_entry = tk.Entry(edit_budget_window)
    income_entry.grid(row=0, column=1, padx=10, pady=5)

    month_issued_label = tk.Label(edit_budget_window, text="Month Issued:")
    month_issued_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")
    selected_months_var = tk.StringVar(edit_budget_window)
    selected_months_var.set(months[0])
    month_issued_menu = tk.OptionMenu(edit_budget_window, selected_months_var, *months)
    month_issued_menu.grid(row=1, column=1, padx=10, pady=5)

    add_categories_label = tk.Label(edit_budget_window, text="Add Categories:")
    add_categories_label.grid(row=2, column=0, padx=10, pady=5, sticky="w")
    add_categories_entry = tk.Entry(edit_budget_window)
    add_categories_entry.grid(row=2, column=1, padx=10, pady=5)

    select_categories_label = tk.Label(edit_budget_window, text="Select Categories:")
    select_categories_label.grid(row=3, column=0, padx=10, pady=5, sticky="w")
    selected_category_var = tk.StringVar(edit_budget_window)
    selected_category_var.set(categories[0])  
    category_menu = tk.OptionMenu(edit_budget_window, selected_category_var, *categories)
    category_menu.grid(row=3, column=1, padx=10, pady=5)

    save_button = tk.Button(edit_budget_window, text="Save", command=save_budget)
    save_button.grid(row=4, column=1)

    #Deletion
    delete_label = tk.Button(edit_budget_window, text="Edit")
    delete_label.grid(row=5, column=0, padx=10, pady=5, sticky="w")
    delete_label = tk.Button(edit_budget_window, text="Edit")
    delete_label.grid(row=5, column=0, padx=10, pady=5, sticky="w")

