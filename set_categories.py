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

# Mei Ting part clear frame b4 open new one
def clear_frame(frame):
    for widget in frame.winfo_children():
        widget.destroy()

def open_set_categories_window(set_categories_frame):
    clear_frame(set_categories_frame)

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
        
    # set_categories_window = CTkToplevel()
    # set_categories_window.title("Set Categories")
    # set_categories_window.geometry("660x470")
    # set_categories_window.resizable(width=False,height=False)
    # set_categories_window.wm_attributes("-topmost",True)
    
    categories_label = CTkLabel(set_categories_frame, text="Categories", font=CTkFont("font/Poppins-Bold.ttf",50,"bold"), text_color="#6965A3" )
    categories_label.place(relx=0.05, rely=0.08, anchor="w")
    
    choose_year_label = CTkLabel(set_categories_frame, text="Select Year of Income:",font=CTkFont("font/Poppins-Bold.ttf",35))
    choose_year_label.place(relx=0.08, rely=0.18, anchor="w")
    year_image = CTkLabel(set_categories_frame, text="",font=CTkFont("font/Poppins-Bold.ttf",35),image= CTkImage(calendar_icon))
    year_image.place(relx=0.05, rely=0.18, anchor="w")
    
    custom_font = CTkFont("font/Poppins-Bold.ttf", size=30)

    choose_year_menu = CTkOptionMenu(set_categories_frame,values=years, font=custom_font, fg_color="#6965A3", button_color="#3F3D65", button_hover_color="#A7A5C9")
    choose_year_menu.place(relx=0.43, rely=0.18, anchor="w")
    
    choose_year_button = CTkButton(set_categories_frame, text="Updates Year", font=CTkFont("font/Poppins-Bold.ttf",30), fg_color="#6965A3", hover_color="#8885B6",image= CTkImage(update_icon),command= choose_year)
    choose_year_button.place(relx=0.66, rely=0.18, anchor="w")
    
    
    choose_month_label = CTkLabel(set_categories_frame, text="Select Month of Income:",font=CTkFont("font/Poppins-Bold.ttf",35))
    choose_month_label.place(relx=0.08, rely=0.26, anchor="w")
    month_image = CTkLabel(set_categories_frame, text="",font=CTkFont("font/Poppins-Bold.ttf",35),image= CTkImage(calendar_icon))
    month_image.place(relx=0.05, rely=0.26, anchor="w")
    
    choose_month_menu = CTkOptionMenu(set_categories_frame,values=months, font=custom_font, fg_color="#6965A3", button_color="#3F3D65", button_hover_color="#A7A5C9")
    choose_month_menu.place(relx=0.43, rely=0.26, anchor="w")
    
    choose_month_button = CTkButton(set_categories_frame, text="Updates Month", font=CTkFont("font/Poppins-Bold.ttf",30), fg_color="#6965A3", hover_color="#8885B6",image= CTkImage(update_icon), command=choose_month)
    choose_month_button.place(relx=0.66, rely=0.26, anchor="w")
    
    #add a new categories
    add_categories_label = CTkLabel(set_categories_frame, text="Add New Categories:",font=CTkFont("font/Poppins-Bold.ttf",35))
    add_categories_label.place(relx=0.08, rely=0.34, anchor="w")

    #Mei Ting's Part : Entry font change
    def add_categories_entry_font_change(event):
        text = add_categories_entry.get
        add_categories_entry.configure(font=CTkFont("font/Poppins.ttf",35))

    add_categories_entry = CTkEntry(set_categories_frame, width=180, height=46)
    add_categories_entry.place(relx=0.43, rely=0.34, anchor="w")
    add_categories_entry.bind("<KeyRelease>", add_categories_entry_font_change)
    add_cat_image = CTkLabel(set_categories_frame, text="",font=CTkFont("font/Poppins-Bold.ttf",35),image= CTkImage(category_icon))
    add_cat_image.place(relx=0.05, rely=0.34, anchor="w")
    
    #save button
    add_categories_save_button = CTkButton(set_categories_frame, text="Save", font=CTkFont("font/Poppins-Bold.ttf",30), image=CTkImage(save_icon), fg_color="#6965A3", hover_color="#8885B6", command=save_1)
    add_categories_save_button.place(relx=0.66, rely=0.34, anchor="w")
    
    #select categories
    select_categories_label = CTkLabel(set_categories_frame, text="Select Categories:",font=CTkFont("font/Poppins-Bold.ttf",35))
    select_categories_label.place(relx=0.08, rely=0.42, anchor="w")
    select_cat_image = CTkLabel(set_categories_frame, text="",font=CTkFont("font/Poppins-Bold.ttf",35),image= CTkImage(category_icon))
    select_cat_image.place(relx=0.05, rely=0.42, anchor="w")
    
    #drop down selected categories menu
    category_menu = CTkOptionMenu(set_categories_frame,values=categories, font=custom_font, fg_color="#6965A3", button_color="#3F3D65", button_hover_color="#A7A5C9")
    category_menu.place(relx=0.43, rely=0.42, anchor="w")
    
    #allocate categories
    allocate_categories_label = CTkLabel(set_categories_frame, text="Allocate Budget (RM):",font=CTkFont("font/Poppins-Bold.ttf",35))
    allocate_categories_label.place(relx=0.08, rely=0.50, anchor="w")

    #Mei Ting's Part : Entry font change
    def allocate_categories_entry_font_change(event):
        text = allocate_categories_entry.get
        allocate_categories_entry.configure(font=CTkFont("font/Poppins.ttf",35))

    allocate_categories_entry = CTkEntry(set_categories_frame, width=180, height=46)
    allocate_categories_entry.place(relx=0.43, rely=0.50, anchor="w")
    allocate_categories_entry.bind("<KeyRelease>", allocate_categories_entry_font_change)
    income_image = CTkLabel(set_categories_frame, text="",font=CTkFont("font/Poppins-Bold.ttf",30),image= CTkImage(expenses_icon))
    income_image.place(relx=0.05, rely=0.50, anchor="w")
    
    #save button 2
    allocate_categories_save_button = CTkButton(set_categories_frame, text="Save", font=CTkFont("font/Poppins-Bold.ttf",30), image=CTkImage(save_icon), fg_color="#6965A3", hover_color="#8885B6", command=save_2)
    allocate_categories_save_button.place(relx=0.66, rely=0.50, anchor="w")

    #frame around deletion
    deletion_frame = CTkFrame(master=set_categories_frame,
                              width=360, height=260,
                              fg_color="#1f2124",border_color="#535085",
                              border_width=4,corner_radius=8)
    deletion_frame.place(relx=0.05, rely=0.68, anchor="w")
    
    #set colour frame
    set_colour_frame = CTkFrame(master=set_categories_frame,
                              width=400, height=260,
                              fg_color="#1f2124",border_color="#535085",
                              border_width=4,corner_radius=8)
    set_colour_frame.place(relx=0.45, rely=0.68, anchor="w")

    #delete category label
    delete_categories_label = CTkLabel(deletion_frame, text="Delete Categories Here",font=CTkFont("font/Poppins-Bold.ttf",30))
    delete_categories_label.place(x=25, rely=0.06, anchor="nw")
    
    #set color label
    color_categories_label = CTkLabel(set_colour_frame, text="Set Colour Here",font=CTkFont("font/Poppins-Bold.ttf",30))
    color_categories_label.place(x=80, rely=0.06, anchor="nw")
    
    #optionmenu for category deletion 
    delete_category_menu = CTkOptionMenu(deletion_frame,values=categories, anchor= CENTER, width=130, height=40, font=custom_font, fg_color="#6965A3", button_color="#3F3D65", button_hover_color="#A7A5C9")
    delete_category_menu.place(x=100, rely=0.25, anchor="nw")
    
    #deletion button
    delete_categories_button = CTkButton(deletion_frame, text="Delete Categories", font=CTkFont("font/Poppins-Bold.ttf",30), image=CTkImage(save_icon), corner_radius=6, fg_color="#6965A3", bg_color="#1f2124", hover_color="#8885B6",command=delete_category)
    delete_categories_button.place(x=37, rely=0.90, anchor="sw")

    #set colours 
    set_colour_button = CTkButton(set_colour_frame, text="Set Categories Colours", font=CTkFont("font/Poppins-Bold.ttf",30), image=CTkImage(save_icon), corner_radius=6, fg_color="#6965A3", bg_color="#1f2124", hover_color="#8885B6",command=category_and_colour_save)
    set_colour_button.place(x=25, rely=0.90, anchor="sw")
    
    #choose categories for color 
    category_to_be_tag_menu = CTkOptionMenu(set_colour_frame, values=categories, anchor= CENTER, width=130, height=40, font=custom_font, fg_color="#6965A3", button_color="#3F3D65", button_hover_color="#A7A5C9")
    category_to_be_tag_menu.place(x=120, rely=0.25, anchor="nw")
    
    colour_to_be_tag_menu = CTkOptionMenu(set_colour_frame, values=colors, anchor= CENTER, width=130, height=40, font=custom_font, fg_color="#6965A3", button_color="#3F3D65", button_hover_color="#A7A5C9")
    colour_to_be_tag_menu.place(x=120, rely=0.50, anchor="nw")
    

    

  

