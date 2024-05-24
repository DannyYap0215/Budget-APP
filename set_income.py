from customtkinter import *
import tkinter as tk
from tkinter import messagebox
import database_test as db
import sqlite3


months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

month_is_saved = False

income_data = []

def open_set_income_window():
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
        month_selected = CTkLabel(set_income_window, text=f"{selected_month_menu}",width=80, height=10)
        month_selected.grid(row=4, column=1)
        
    def save_year():

        selected_year = year_entry.get()
        year_selected = CTkLabel(set_income_window, text=f"{selected_year}",width=80, height=10)
        year_selected.grid(row=3, column=1,pady=(30,0))
        
    set_income_window = CTkToplevel()
    set_income_window.title("Set Income")
    set_income_window.geometry("450x300")
    set_income_window.wm_attributes("-topmost",True)
    set_income_window.resizable(width=False, height=False)
    
    year_label = CTkLabel(set_income_window, text="Year:")
    year_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")
    year_entry = CTkEntry(set_income_window)
    year_entry.grid(row=0, column=1, padx=10, pady=5)
    
    income_label = CTkLabel(set_income_window, text="Income:")
    income_label.grid(row=2, column=0, padx=10, pady=5, sticky="w")
    income_entry = CTkEntry(set_income_window)
    income_entry.grid(row=2, column=1, padx=10, pady=5)
  
    month_issued_label = CTkLabel(set_income_window, text="Month Issued:")
    month_issued_label.grid(row=1, column=0, padx=10, pady=(5,30), sticky="w")
    month_issued_menu = CTkOptionMenu(set_income_window, values=months,anchor= CENTER) 
    month_issued_menu.grid(row=1, column=1, padx=10, pady=(5,30))
    
    choose_month_button = CTkButton(set_income_window, text="Confirm Month ", command=save_month)
    choose_month_button.grid(row=1, column=2, padx=10, pady=(5,30))
    
    choose_year_button = CTkButton(set_income_window, text="Confirm Year", command=save_year)
    choose_year_button.grid(row=0, column=2)
  
    save_button = CTkButton(set_income_window, text="Save ALL", command=save_budget)
    save_button.grid(row=2, column=2, padx=10, pady=5)
    
    income_data.append((selected_month_menu, income_allocated))

    year_selection = CTkLabel(set_income_window, text=f"Year Selected:")
    year_selection.grid(row=3,column=0, pady=(30,0))
    
    month_selection = CTkLabel(set_income_window, text=f"Month Selected:")
    month_selection.grid(row=4,column=0, padx=(7,0))
    





