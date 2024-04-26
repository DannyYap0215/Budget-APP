from customtkinter import *
import tkinter as tk
from tkinter import messagebox


months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

month_is_saved = False

def open_set_income_window():
    def save_budget():
        global selected_month_menu
        income_allocated = income_entry.get()
        if month_is_saved == True:
            if income_allocated.strip() != "" and selected_month_menu == month_issued_menu.get() and income_allocated.isdigit() == True:
                print((income_allocated,selected_month_menu))
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
        month_selected = CTkLabel(set_income_window, text=f"{selected_month_menu}",width=50, height=10)
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
    
    month_selection = CTkLabel(set_income_window, text=f"Month Selected:")
    month_selection.grid(row=5,column=0)
    





