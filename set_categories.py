import tkinter as tk

categories = [
    "Rent",
    "Utility",
    "Food"
]

def open_set_categories_window():
    global categories
    
    def save_budget():
        new_category = add_categories_entry.get()
        if new_category not in categories and new_category != "":
            categories.append(new_category) #set the entry text as Var, so it can be added as a menu 
            category_menu['menu'].add_command(command=tk._setit(selected_category_var, add_categories_entry.get()), label=add_categories_entry.get())
            add_categories_entry.delete(0, 'end') #deletes from the first index to the end of the widget entry 
        else:
            pass

    set_categories_window = tk.Toplevel()
    set_categories_window.title("Set Categories")
    set_categories_window.geometry("400x300")

    add_categories_label = tk.Label(set_categories_window, text="Add Categories:")
    add_categories_label.grid(row=2, column=0, padx=10, pady=5, sticky="w")
    add_categories_entry = tk.Entry(set_categories_window)
    add_categories_entry.grid(row=2, column=1, padx=10, pady=5)

    select_categories_label = tk.Label(set_categories_window, text="Select Categories:")
    select_categories_label.grid(row=3, column=0, padx=10, pady=5, sticky="w")
    selected_category_var = tk.StringVar(set_categories_window)
    selected_category_var.set(categories[0])  
    category_menu = tk.OptionMenu(set_categories_window, selected_category_var, *categories)
    category_menu.grid(row=3, column=1, padx=10, pady=5)

    save_button = tk.Button(set_categories_window, text="Save", command=save_budget)
    save_button.grid(row=4, column=1)



