from customtkinter import *
from set_income import months
from tkinter import messagebox
import database_test as db


colors = [
    "red",
    "green",
    "blue",
    "yellow",
    "orange",
    "purple",
    "pink",
    "brown",
    "cyan",
    "magenta",
    "black",
    "white",
    "gray",
    "lightgray",
    "darkgray",
    "lightblue",
    "darkblue",
    "lightgreen",
    "darkgreen",
    "lightred",
    "darkred",
    "lightyellow",
    "darkyellow",
    "lightorange",
    "darkorange",
    "lightpurple",
    "darkpurple"
]


allocated=[]
categories = db.update_categories_list()
list_for_coloured_categories = []
month_is_choosen = False
#add categories then save ; then select categories and add individual budget 
def open_set_categories_window():
    global categories
    
    def save_1():
        new_category = add_categories_entry.get()
        if new_category != "" and month_is_choosen == True and month_choosen == choose_month_menu.get():
            if new_category.strip(): 
                if new_category not in categories:
                    categories.append(new_category) 
                    category_menu.configure(values=categories)
                    delete_category_menu.configure(values=categories)
                    category_to_be_tag_menu.configure(values=categories)
                    add_categories_entry.delete(0, 'end')
                    db.add_new_categories(new_category)
                else:
                    messagebox.showerror("Error", "Category already exists!")
            elif new_category.strip() == False :
                messagebox.showerror("Error", "Please enter a non-empty category!")
        elif month_is_choosen == False:
            messagebox.showerror("Error", "Please choose a month first!")
        elif month_is_choosen == True and month_choosen != choose_month_menu.get():
            messagebox.showerror("Error", "Please check if you selected a month correctly!")

        
    def save_2():
        allocated_budget = allocate_categories_entry.get()
        category_selected = category_menu.get()
        if allocated_budget not in allocated and allocated_budget != "":
            allocated.append(allocated_budget) 
            print(category_selected, allocated_budget)
            allocate_categories_entry.delete(0, 'end')
        else:
            pass
        
    def delete_category():
        category_to_delete = delete_category_menu.get()
        if category_to_delete in categories:
            categories.remove(category_to_delete)
        #configure = updates 
        category_menu.configure(values=categories) 
        delete_category_menu.configure(values=categories)
        category_to_be_tag_menu.configure(values=categories)
        
    def choose_month():
        global month_is_choosen,month_choosen,categories,category_for_colour,colour_for_category
        month_choosen = choose_month_menu.get()
        print(month_choosen)
        month_is_choosen = True
        categories = db.update_categories_list()
        category_menu.configure(values=categories)  # Use the widgets from set_categories module
        delete_category_menu.configure(values=categories)
        category_to_be_tag_menu.configure(values=categories)
        
    
    def category_and_colour_save():
        global colour_for_category, category_for_colour,month_choosen
        colour_for_category = colour_to_be_tag_menu.get()
        category_for_colour = category_to_be_tag_menu.get()
        
        list_for_coloured_categories.append((colour_for_category,category_for_colour))
        print(list_for_coloured_categories)
        
        db.add_new_colour(colour_for_category,category_for_colour)
        
        
        
    set_categories_window = CTkToplevel()
    set_categories_window.title("Set Categories")
    set_categories_window.geometry("360x500")
    set_categories_window.resizable(width=False,height=False)
    set_categories_window.wm_attributes("-topmost",True)
    
    
    choose_month_label = CTkLabel(set_categories_window, text="Select Month of Income:")
    choose_month_label.grid(row=2, column=0, padx=10, pady=5, sticky="w")
    
    choose_month_menu = CTkOptionMenu(set_categories_window,values=months)
    choose_month_menu.grid(row=2, column=1, padx=10, pady=5)
    
    choose_month_button = CTkButton(set_categories_window, text="Confirm Month", command=choose_month)
    choose_month_button.grid(row=3, column=1)
    
    #add a new categories
    add_categories_label = CTkLabel(set_categories_window, text="Add New Categories:")
    add_categories_label.grid(row=4, column=0, padx=10, pady=5, sticky="w")
    add_categories_entry = CTkEntry(set_categories_window)
    add_categories_entry.grid(row=4, column=1, padx=10, pady=5)
    
    #save button
    add_categories_save_button = CTkButton(set_categories_window, text="Save", command=save_1)
    add_categories_save_button.grid(row=5, column=1)
    
    #select categories
    select_categories_label = CTkLabel(set_categories_window, text="Select Categories:")
    select_categories_label.grid(row=6, column=0, padx=10, pady=5, sticky="w")
    
    #drop down selected categories menu
    category_menu = CTkOptionMenu(set_categories_window,values=categories)
    category_menu.grid(row=6, column=1, padx=10, pady=5)
    
    #allocate categories
    allocate_categories_label = CTkLabel(set_categories_window, text="Allocate Budget:")
    allocate_categories_label.grid(row=7, column=0, padx=10, pady=5, sticky="w")
    allocate_categories_entry = CTkEntry(set_categories_window)
    allocate_categories_entry.grid(row=7, column=1, padx=10, pady=5)
    
    #save button 2
    allocate_categories_save_button = CTkButton(set_categories_window, text="Save", command=save_2)
    allocate_categories_save_button.grid(row=8, column=1)

    #frame around deletion
    deletion_frame = CTkFrame(master=set_categories_window,
                              width=170,height= 180,
                              fg_color="#1f2124",border_color="purple",
                              border_width=4,corner_radius=8)
    deletion_frame.grid(row=9, column=0,padx=(10,1),pady=(20,0))
    
    #set colour frame
    set_colour_frame = CTkFrame(master=set_categories_window,
                              width=170,height= 180,
                              fg_color="#1f2124",border_color="purple",
                              border_width=4,corner_radius=8)
    set_colour_frame.grid(row=9, column=1,padx=(1,10),pady=(20,0))

    #delete category label
    delete_categories_label = CTkLabel(set_categories_window, text="Delete Categories Here", fg_color ="#1f2124")
    delete_categories_label.place(x=18, rely=0.05, anchor="nw", in_=deletion_frame)
    
    #set color label
    color_categories_label = CTkLabel(set_categories_window, text="Set Colour Here", fg_color ="#1f2124")
    color_categories_label.place(x=40, rely=0.05, anchor="nw", in_=set_colour_frame)
    
    #optionmenu for category deletion 
    delete_category_menu = CTkOptionMenu(set_categories_window,values=categories,width=130,height=40)
    delete_category_menu.place(x=18, rely=0.2, anchor="nw", in_=deletion_frame)
    
    #deletion button
    delete_categories_button = CTkButton(set_categories_window, text="Delete Categories", corner_radius=6, bg_color="#1f2124",command=delete_category)
    delete_categories_button.place(x=14, rely=0.95, anchor="sw", in_=deletion_frame)

    #set colours 
    set_colour_button = CTkButton(set_categories_window, text="Set Categories Colours", corner_radius=6, bg_color="#1f2124",command=category_and_colour_save)
    set_colour_button.place(x=14, rely=0.95, anchor="sw", in_=set_colour_frame)
    
    #choose categories for color 
    category_to_be_tag_menu = CTkOptionMenu(set_categories_window,values=categories,width=130,height=40)
    category_to_be_tag_menu.place(x=18, rely=0.2, anchor="nw", in_=set_colour_frame)
    
    colour_to_be_tag_menu = CTkOptionMenu(set_categories_window,values=colors,width=130,height=40)
    colour_to_be_tag_menu.place(x=18, rely=0.5, anchor="nw", in_=set_colour_frame)
    

    

  

