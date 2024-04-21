from customtkinter import *
import tkinter as tk


months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]



def open_set_income_window():

    def save_budget():
        set_income_window.destroy()

    set_income_window = CTkToplevel()
    set_income_window.title("Set Income")
    set_income_window.geometry("400x300")

    income_label = CTkLabel(set_income_window, text="Income:")
    income_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")
    income_entry = CTkEntry(set_income_window)
    income_entry.grid(row=0, column=1, padx=10, pady=5)
  
    month_issued_label = CTkLabel(set_income_window, text="Month Issued:")
    month_issued_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")
    month_issued_menu = CTkOptionMenu(set_income_window, values=months) # ctk does not need Var now, just write value= //list//
    month_issued_menu.grid(row=1, column=1, padx=10, pady=5)
  
    save_button = CTkButton(set_income_window, text="Save", command=save_budget)
    save_button.grid(row=4, column=1)





