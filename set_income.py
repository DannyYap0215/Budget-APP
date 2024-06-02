from customtkinter import *
import tkinter as tk
from tkinter import messagebox
import database_test as db
import sqlite3
from PIL import Image

months = ["January",
          "February", 
          "March", 
          "April", 
          "May", "June", 
          "July", "August", 
          "September", 
          "October", 
          "November", 
          "December"]

month_is_saved = False

income_data = []
calendar_icon = Image.open("icon/calendar_icon.png")
expenses_icon = Image.open("icon/expenses_icon.png")
save_icon = Image.open("icon/saved_icon.png")
update_icon = Image.open("icon/update_icon.png")
selected_icon = Image.open("icon/selected.png")

def clear_frame(frame):
    for widget in frame.winfo_children():
        widget.destroy()

def open_set_income_window(set_income_frame):
    clear_frame(set_income_frame)

    global selected_month_menu  # Define selected_month_menu as a global variable
    selected_month_menu = None  # Initialize selected_month_menu
    global income_allocated  # Define income_allocated as a global variable
    income_allocated = None  # Initialize income_allocated
    
    def save_budget():
        global selected_month_menu
        global income_allocated  
        
        selected_month_menu = month_issued_menu.get()
        income_allocated = income_entry.get()
        selected_year = year_entry.get()

        if month_is_saved:
            selected_month_menu = month_issued_menu.get()
            selected_year = year_entry.get()  

            if selected_year.strip():  
                con = sqlite3.connect("database.db")
                c = con.cursor()
                c.execute("SELECT year FROM allocated_income_for_month_2024 WHERE year=?", (selected_year,))
                existing_year = c.fetchone()

                if existing_year:
                    print(f"The year {selected_year} already exists in the database.")
                else:
                    print(f"The year {selected_year} does not exist in the database.")
                    c.executemany("INSERT INTO allocated_income_for_month_2024 (months, year, allocated_income) VALUES (?, ?, ?)",
                                [(month, selected_year, income_allocated if month == selected_month_menu else 0) for month in months])
                    con.commit()  
                    
                    
                if income_allocated.strip() != "" and income_allocated.isdigit():
                    print((income_allocated, selected_month_menu,selected_year))
                    table_name = "allocated_income_for_month_2024"
                    c.execute(f"UPDATE {table_name} SET allocated_income = ? WHERE months = ? AND year = ?", (income_allocated, selected_month_menu, selected_year))
                    con.commit()
                elif income_allocated.strip() == "":
                    messagebox.showerror("Error", "Please enter a non-empty value!")
                elif not income_allocated.isdigit():
                    messagebox.showerror("Error", "Please check if you've entered a digit!")
            else:
                messagebox.showerror("Error", "Please enter a year!")
        else:
            messagebox.showerror("Error", "Please choose a month first!")


    def save_month():
        global month_is_saved
        global selected_month_menu
        global month_selected

        selected_month_menu = month_issued_menu.get()
        month_is_saved = True
        month_selected = CTkLabel(set_income_frame, text=f"{selected_month_menu}",font=CTkFont("font/Poppins-Bold.ttf",20),width=80, height=10)
        month_selected.place(relx=0.15, rely=0.58, anchor="w")
        
    def save_year():

        selected_year = year_entry.get()
        year_selected = CTkLabel(set_income_frame, text=f"{selected_year}",font=CTkFont("font/Poppins-Bold.ttf",20),width=80, height=10)
        year_selected.place(relx=0.15, rely=0.5, anchor="w")
        
    # set_income_window = CTkToplevel()
    # set_income_window.title("Set Income")
    # set_income_window.geometry("620x320")
    # set_income_window.wm_attributes("-topmost",True)
    # set_income_window.resizable(width=False, height=False)
    
    set_income_label = CTkLabel(set_income_frame, text="Set Income", font=CTkFont("font/Poppins-Bold.ttf",50,"bold") , text_color="#6965A3")
    set_income_label.place(relx=0.05, rely=0.08, anchor="w")
    
    year_label = CTkLabel(set_income_frame, text="Enter Year:",font=CTkFont("font/Poppins-Bold.ttf",35))
    year_label.place(relx=0.08, rely=0.18, anchor="w")

    #Mei Ting's Part : Entry font change
    def year_entry_font_change(event):
        text = year_entry.get
        year_entry.configure(font=CTkFont("font/Poppins.ttf",35))

    year_entry = CTkEntry(set_income_frame, width=180, height=46)
    year_entry.place(relx=0.35, rely=0.18, anchor="w")
    year_entry.bind("<KeyRelease>", year_entry_font_change)

    year_image = CTkLabel(set_income_frame, text="",font=CTkFont("font/Poppins-Bold.ttf",35),image= CTkImage(calendar_icon))
    year_image.place(relx=0.05, rely=0.18, anchor="w")
    
    income_label = CTkLabel(set_income_frame, text="Allocate Income:",font=CTkFont("font/Poppins-Bold.ttf",35))
    income_label.place(relx=0.08, rely=0.34, anchor="w")

    #Mei Ting's Part : Entry font change
    def income_entry_font_change(event):
        text = income_entry.get
        income_entry.configure(font=CTkFont("font/Poppins.ttf",35))

    income_entry = CTkEntry(set_income_frame, width=180, height=46)
    income_entry.place(relx=0.35, rely=0.34, anchor="w")
    income_entry.bind("<KeyRelease>", income_entry_font_change)

    income_image = CTkLabel(set_income_frame, text="",font=CTkFont("font/Poppins-Bold.ttf",35),image= CTkImage(expenses_icon))
    income_image.place(relx=0.05, rely=0.34, anchor="w")
  
    custom_font = CTkFont("font/Poppins-Bold.ttf", size=30)

    month_issued_label = CTkLabel(set_income_frame, text="Month Issued:",font=CTkFont("font/Poppins-Bold.ttf",35))
    month_issued_label.place(relx=0.08, rely=0.26, anchor="w")
    month_issued_menu = CTkOptionMenu(set_income_frame, values=months, anchor= CENTER, font=custom_font, fg_color="#6965A3", bg_color="#1f2124", button_color="#3F3D65", button_hover_color="#A7A5C9") 
    month_issued_menu.place(relx=0.35, rely=0.26, anchor="w")
    month_image = CTkLabel(set_income_frame, text="",font=CTkFont("font/Poppins-Bold.ttf",35),image= CTkImage(calendar_icon))
    month_image.place(relx=0.05, rely=0.26, anchor="w")
    
    choose_month_button = CTkButton(set_income_frame, text="Updates Month ", font=CTkFont("font/Poppins-Bold.ttf",30), fg_color="#6965A3", bg_color="#1f2124",image= CTkImage(update_icon), command=save_month)
    choose_month_button.place(relx=0.58, rely=0.26, anchor="w")
    
    choose_year_button = CTkButton(set_income_frame, text="Updates Year", font=CTkFont("font/Poppins-Bold.ttf",30), fg_color="#6965A3", bg_color="#1f2124",image= CTkImage(update_icon), command=save_year)
    choose_year_button.place(relx=0.58, rely=0.18, anchor="w")
  
    save_button = CTkButton(set_income_frame, text="Save ALL", font=CTkFont("font/Poppins-Bold.ttf",30), image=CTkImage(save_icon), fg_color="#6965A3", bg_color="#1f2124", command=save_budget)
    save_button.place(relx=0.58, rely=0.34, anchor="w")
    
    income_data.append((selected_month_menu, income_allocated))

    year_selection_icon = CTkLabel(set_income_frame, text="", image= CTkImage(selected_icon))
    year_selection_icon.place(relx=0.05, rely=0.5, anchor="w")
    year_selection = CTkLabel(set_income_frame, text=f"Year Selected:",font=CTkFont("font/Poppins-Bold.ttf",35))
    year_selection.place(relx=0.08, rely=0.5, anchor="w")
    
    month_selection_icon = CTkLabel(set_income_frame, text="", image= CTkImage(selected_icon))
    month_selection_icon.place(relx=0.05, rely=0.58, anchor="w")
    month_selection = CTkLabel(set_income_frame, text=f"Month Selected:",font=CTkFont("font/Poppins-Bold.ttf",35))
    month_selection.place(relx=0.08, rely=0.58, anchor="w")