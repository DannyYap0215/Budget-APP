from customtkinter import *
import customtkinter
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
        if new_category.strip():
            if new_category not in categories and new_category != "":
                categories.append(new_category) 
                category_menu.configure(values=categories) #3hrs wasted here; switched to CTk and searched whole internet on how to add a value to the menu, not 1 tutorial exist - danny with 3hrs wasted(fixed with configure)
                add_categories_entry.delete(0, 'end') #deletes from the first index to the end of the widget entry 
            else:
                pass
        
    def save_2():
        allocated_budget = allocate_categories_entry.get()
        category_selected = category_menu.get()
        if allocated_budget not in allocated and allocated_budget != "":
            allocated.append(allocated_budget) 
            print(category_selected, allocated_budget)
            allocate_categories_entry.delete(0, 'end')
        else:
            pass

    set_categories_window = CTkToplevel()
    set_categories_window.title("Set Categories")
    set_categories_window.geometry("400x300")
    #add a new categories
    add_categories_label = CTkLabel(set_categories_window, text="Add New Categories:")
    add_categories_label.grid(row=2, column=0, padx=10, pady=5, sticky="w")
    add_categories_entry = CTkEntry(set_categories_window)
    add_categories_entry.grid(row=2, column=1, padx=10, pady=5)
    #save button
    add_categories_save_button = CTkButton(set_categories_window, text="Save", command=save_1)
    add_categories_save_button.grid(row=3, column=1)
    #select categories
    select_categories_label = CTkLabel(set_categories_window, text="Select Categories:")
    select_categories_label.grid(row=4, column=0, padx=10, pady=5, sticky="w")
    #drop down selected categories menu
    category_menu = CTkOptionMenu(set_categories_window,values=categories)
    category_menu.grid(row=4, column=1, padx=10, pady=5)
    #allocate categories
    allocate_categories_label = CTkLabel(set_categories_window, text="Allocate Budget:")
    allocate_categories_label.grid(row=5, column=0, padx=10, pady=5, sticky="w")
    allocate_categories_entry = CTkEntry(set_categories_window)
    allocate_categories_entry.grid(row=5, column=1, padx=10, pady=5)
    #save button 2
    allocate_categories_save_button = CTkButton(set_categories_window, text="Save", command=save_2)
    allocate_categories_save_button.grid(row=6, column=1)

    



