from customtkinter import *
from set_income import months
from tkinter import messagebox
import database_test as db
import sqlite3
from PIL import Image


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

save_icon = Image.open("icon/saved_icon.png")
calendar_icon = Image.open("icon/calendar_icon.png")
expenses_icon = Image.open("icon/expenses_icon.png")
category_icon = Image.open("icon/category_icon.png")
update_icon = Image.open("icon/update_icon.png")

allocated=[]
categories = db.update_categories_list()
list_for_coloured_categories = []
month_is_choosen = False
#add categories then save ; then select categories and add individual budget 
def open_set_categories_window():
    global categories
    
    def save_1(): #adding new categories
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

        
    def save_2(): #allocate budget
        allocated_budget = allocate_categories_entry.get()
        category_selected = category_menu.get()
        if allocated_budget != "":
            allocated.append(allocated_budget) 
            print(category_selected, allocated_budget)
            allocate_categories_entry.delete(0, 'end')
            db.allocating_budget_to_table(month_choosen,allocated_budget,category_selected,year_choosen)
        else:
            pass
        
    def delete_category():
        category_to_delete = delete_category_menu.get()
        db.delete_categories(category_to_delete)
        categories = db.update_categories_list()
        category_menu.configure(values=categories) 
        delete_category_menu.configure(values=categories)
        category_to_be_tag_menu.configure(values=categories)
        
        
    def choose_month():
        global month_is_choosen,month_choosen,categories,category_for_colour,colour_for_category
        month_choosen = choose_month_menu.get()
        print(month_choosen)
        month_is_choosen = True
        categories = db.update_categories_list()
        category_menu.configure(values=categories)  
        delete_category_menu.configure(values=categories)
        category_to_be_tag_menu.configure(values=categories)
        
    
    def category_and_colour_save():
        global colour_for_category, category_for_colour,month_choosen
        colour_for_category = colour_to_be_tag_menu.get()
        category_for_colour = category_to_be_tag_menu.get()
        
        list_for_coloured_categories.append((colour_for_category,category_for_colour))
        print(list_for_coloured_categories)
        
        db.add_new_colour(colour_for_category,category_for_colour)
        
    def choose_year():
        global year_choosen
        year_choosen = choose_year_menu.get()
        print(year_choosen)

    con = sqlite3.connect("database.db")
    c = con.cursor()
    c.execute("SELECT DISTINCT year FROM allocated_income_for_month_2024")
    years = c.fetchall()
    years = [str(year[0]) for year in years]
        
    set_categories_window = CTkToplevel()
    set_categories_window.title("Set Categories")
    set_categories_window.geometry("660x470")
    set_categories_window.resizable(width=False,height=False)
    set_categories_window.wm_attributes("-topmost",True)
    
    categories_label = CTkLabel(set_categories_window, text="Categories", font=CTkFont("font/Poppins-Bold.ttf",50,"bold"), text_color="#6965A3" )
    categories_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")
    
    choose_year_label = CTkLabel(set_categories_window, text="Select Year of Income:",font=CTkFont("font/Poppins-Bold.ttf",20))
    choose_year_label.grid(row=1, column=0, padx=40, pady=5, sticky="w")
    year_image = CTkLabel(set_categories_window, text="",font=CTkFont("font/Poppins-Bold.ttf",20),image= CTkImage(calendar_icon))
    year_image.grid(row=1, column=0, padx=10, pady=5, sticky="w")
    
    choose_year_menu = CTkOptionMenu(set_categories_window,values=years,anchor= CENTER ,fg_color="#6965A3")
    choose_year_menu.grid(row=1, column=1, padx=10, pady=5)
    
    choose_year_button = CTkButton(set_categories_window, text="Updates Year", fg_color="#6965A3",hover_color="#8885B6",image= CTkImage(update_icon),command= choose_year)
    choose_year_button.grid(row=1, column=2)
    
    
    choose_month_label = CTkLabel(set_categories_window, text="Select Month of Income:",font=CTkFont("font/Poppins-Bold.ttf",20))
    choose_month_label.grid(row=3, column=0, padx=40, pady=5, sticky="w")
    month_image = CTkLabel(set_categories_window, text="",font=CTkFont("font/Poppins-Bold.ttf",20),image= CTkImage(calendar_icon))
    month_image.grid(row=3, column=0, padx=10, pady=5, sticky="w")
    
    choose_month_menu = CTkOptionMenu(set_categories_window,values=months,anchor= CENTER, fg_color="#6965A3")
    choose_month_menu.grid(row=3, column=1, padx=10, pady=5)
    
    choose_month_button = CTkButton(set_categories_window, text="Updates Month", fg_color="#6965A3",hover_color="#8885B6",image= CTkImage(update_icon), command=choose_month)
    choose_month_button.grid(row=3, column=2)
    
    #add a new categories
    add_categories_label = CTkLabel(set_categories_window, text="Add New Categories:",font=CTkFont("font/Poppins-Bold.ttf",20))
    add_categories_label.grid(row=5, column=0, padx=40, pady=5, sticky="w")
    add_categories_entry = CTkEntry(set_categories_window)
    add_categories_entry.grid(row=5, column=1, padx=10, pady=5)
    add_cat_image = CTkLabel(set_categories_window, text="",font=CTkFont("font/Poppins-Bold.ttf",20),image= CTkImage(category_icon))
    add_cat_image.grid(row=5, column=0, padx=10, pady=5, sticky="w")
    
    #save button
    add_categories_save_button = CTkButton(set_categories_window, text="Save",image=CTkImage(save_icon), fg_color="#6965A3",hover_color="#8885B6", command=save_1)
    add_categories_save_button.grid(row=5, column=2)
    
    #select categories
    select_categories_label = CTkLabel(set_categories_window, text="Select Categories:",font=CTkFont("font/Poppins-Bold.ttf",20))
    select_categories_label.grid(row=7, column=0, padx=40, pady=5, sticky="w")
    select_cat_image = CTkLabel(set_categories_window, text="",font=CTkFont("font/Poppins-Bold.ttf",20),image= CTkImage(category_icon))
    select_cat_image.grid(row=7, column=0, padx=10, pady=5, sticky="w")
    
    #drop down selected categories menu
    category_menu = CTkOptionMenu(set_categories_window,values=categories,anchor= CENTER, fg_color="#6965A3")
    category_menu.grid(row=7, column=1, padx=10, pady=(5,0))
    
    #allocate categories
    allocate_categories_label = CTkLabel(set_categories_window, text="Allocate Budget:",font=CTkFont("font/Poppins-Bold.ttf",20))
    allocate_categories_label.grid(row=8, column=0, padx=40, pady=5, sticky="w")
    allocate_categories_entry = CTkEntry(set_categories_window)
    allocate_categories_entry.grid(row=8, column=1, padx=10, pady=5)
    income_image = CTkLabel(set_categories_window, text="",font=CTkFont("font/Poppins-Bold.ttf",20),image= CTkImage(expenses_icon))
    income_image.grid(row=8, column=0, padx=10, pady=5, sticky="w")
    
    #save button 2
    allocate_categories_save_button = CTkButton(set_categories_window, text="Save",image=CTkImage(save_icon), fg_color="#6965A3",hover_color="#8885B6", command=save_2)
    allocate_categories_save_button.grid(row=8, column=2)

    #frame around deletion
    deletion_frame = CTkFrame(master=set_categories_window,
                              width=200,height= 180,
                              fg_color="#1f2124",border_color="#535085",
                              border_width=4,corner_radius=8)
    deletion_frame.grid(row=10, column=0,padx=(10,1),pady=(20,0))
    
    #set colour frame
    set_colour_frame = CTkFrame(master=set_categories_window,
                              width=200,height= 180,
                              fg_color="#1f2124",border_color="#535085",
                              border_width=4,corner_radius=8)
    set_colour_frame.grid(row=10, column=1,padx=(1,10),pady=(20,0))

    #delete category label
    delete_categories_label = CTkLabel(deletion_frame, text="Delete Categories Here",font=CTkFont("font/Poppins-Bold.ttf",15))
    delete_categories_label.place(x=25, rely=0.05, anchor="nw")
    
    #set color label
    color_categories_label = CTkLabel(set_colour_frame, text="Set Colour Here",font=CTkFont("font/Poppins-Bold.ttf",15))
    color_categories_label.place(x=50, rely=0.05, anchor="nw")
    
    #optionmenu for category deletion 
    delete_category_menu = CTkOptionMenu(deletion_frame,values=categories,anchor= CENTER,width=130,height=40, fg_color="#6965A3")
    delete_category_menu.place(x=35, rely=0.2, anchor="nw")
    
    #deletion button
    delete_categories_button = CTkButton(deletion_frame, text="Delete Categories",image=CTkImage(save_icon), corner_radius=6, fg_color="#6965A3", bg_color="#1f2124",hover_color="#8885B6",command=delete_category)
    delete_categories_button.place(x=27, rely=0.95, anchor="sw")

    #set colours 
    set_colour_button = CTkButton(set_colour_frame, text="Set Categories Colours",image=CTkImage(save_icon), corner_radius=6, fg_color="#6965A3", bg_color="#1f2124",hover_color="#8885B6",command=category_and_colour_save)
    set_colour_button.place(x=15, rely=0.95, anchor="sw")
    
    #choose categories for color 
    category_to_be_tag_menu = CTkOptionMenu(set_colour_frame,values=categories,anchor= CENTER,width=130,height=40, fg_color="#6965A3")
    category_to_be_tag_menu.place(x=35, rely=0.2, anchor="nw")
    
    colour_to_be_tag_menu = CTkOptionMenu(set_colour_frame,values=colors,anchor= CENTER,width=130,height=40, fg_color="#6965A3")
    colour_to_be_tag_menu.place(x=35, rely=0.5, anchor="nw")
    

    

  

