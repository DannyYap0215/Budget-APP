import tkinter as tk

categories = [
    "Rent",
    "Utility",
    "Food"
]

allocated=[]
#add categories then save ; then select categories and add individual budget 
def open_set_categories_window():
    global categories
    
    def save_1():
        new_category = add_categories_entry.get()
        if new_category not in categories and new_category != "":
            categories.append(new_category) #set the entry text as Var, so it can be added as a menu 
            category_menu['menu'].add_command(command=tk._setit(selected_category_var, add_categories_entry.get()), label=add_categories_entry.get())
            add_categories_entry.delete(0, 'end') #deletes from the first index to the end of the widget entry 
        else:
            pass
        
    def save_2():
        allocated_budget = allocate_categories_entry.get()
        if allocated_budget not in allocated and allocated_budget != "":
            allocated.append(allocated_budget) 
            print(allocated)
            allocate_categories_entry.delete(0, 'end')
        else:
            pass

    set_categories_window = tk.Toplevel()
    set_categories_window.title("Set Categories")
    set_categories_window.geometry("400x300")
    #add a new categories
    add_categories_label = tk.Label(set_categories_window, text="Add New Categories:")
    add_categories_label.grid(row=2, column=0, padx=10, pady=5, sticky="w")
    add_categories_entry = tk.Entry(set_categories_window)
    add_categories_entry.grid(row=2, column=1, padx=10, pady=5)
    #save button
    add_categories_save_button = tk.Button(set_categories_window, text="Save", command=save_1)
    add_categories_save_button.grid(row=3, column=1)
    #select categories
    select_categories_label = tk.Label(set_categories_window, text="Select Categories:")
    select_categories_label.grid(row=4, column=0, padx=10, pady=5, sticky="w")
    #drop down selected categories menu
    selected_category_var = tk.StringVar(set_categories_window)
    selected_category_var.set(categories[0])  
    category_menu = tk.OptionMenu(set_categories_window, selected_category_var, *categories)
    category_menu.grid(row=4, column=1, padx=10, pady=5)
    #allocate categories
    allocate_categories_label = tk.Label(set_categories_window, text="Allocate Budget:")
    allocate_categories_label.grid(row=5, column=0, padx=10, pady=5, sticky="w")
    allocate_categories_entry = tk.Entry(set_categories_window)
    allocate_categories_entry.grid(row=5, column=1, padx=10, pady=5)
    #save button 2
    allocate_categories_save_button = tk.Button(set_categories_window, text="Save", command=save_2)
    allocate_categories_save_button.grid(row=6, column=1)

    



