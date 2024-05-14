from customtkinter import *
import tkinter as tk
from tkinter import messagebox
import database_test as db


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
        global income_allocated  # Access the global variable income_allocated
        
        # Update selected_month_menu and income_allocated
        selected_month_menu = month_issued_menu.get()
        income_allocated = income_entry.get()

        # Check if both month and income are selected
        if selected_month_menu is not None and income_allocated.strip() != "":
            # Append data to income_data
            income_data.append((selected_month_menu, income_allocated))
            # Print for debugging purposes
            print((selected_month_menu, income_allocated))
        else:
            messagebox.showerror("Error", "Please select a month and enter income!")

        if month_is_saved == True:
            if income_allocated.strip() != "" and selected_month_menu == month_issued_menu.get() and income_allocated.isdigit() == True:
                print((income_allocated,selected_month_menu))
                db.allocated_income_for_month(income_allocated,selected_month_menu)
            elif income_allocated.strip() != "" and selected_month_menu != month_issued_menu.get() :
                messagebox.showerror("Error", "Please check if you selected a month correctly!")
            elif income_allocated.strip() == "" :
                messagebox.showerror("Error", "Please enter a non-empty value!")
            elif income_allocated.isdigit() == False :
                messagebox.showerror("Error", "Please check if you've entered a digit!")
        elif month_is_saved == False:
            messagebox.showerror("Error", "Please choose a month first!")


    def save_month():
        global month_is_saved
        global selected_month_menu
        global month_selected

        selected_month_menu = month_issued_menu.get()
        month_is_saved = True
        month_selected = CTkLabel(set_income_window, text=f"{selected_month_menu}",width=80, height=10)
        month_selected.grid(row=5, column=1)
        
    set_income_window = CTkToplevel()
    set_income_window.title("Set Income")
    set_income_window.geometry("400x300")
    set_income_window.wm_attributes("-topmost",True)
    set_income_window.resizable(width=False, height=False)

    income_label = CTkLabel(set_income_window, text="Income:")
    income_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")
    income_entry = CTkEntry(set_income_window)
    income_entry.grid(row=0, column=1, padx=10, pady=5)
  
    month_issued_label = CTkLabel(set_income_window, text="Month Issued:")
    month_issued_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")
    month_issued_menu = CTkOptionMenu(set_income_window, values=months,anchor= CENTER) 
    month_issued_menu.grid(row=1, column=1, padx=10, pady=5)
    
    choose_month_button = CTkButton(set_income_window, text="Confirm Month", command=save_month)
    choose_month_button.grid(row=2, column=1, padx=10, pady=5)
  
    save_button = CTkButton(set_income_window, text="Save ALL", command=save_budget)
    save_button.grid(row=4, column=1)
    
    income_data.append((selected_month_menu, income_allocated))

    month_selection = CTkLabel(set_income_window, text=f"Month Selected:")
    month_selection.grid(row=5,column=0)
    





