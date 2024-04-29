from customtkinter import *
from tkcalendar import DateEntry
from tkinter import ttk
import update_expenses

month = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
]

def open_expenses_history_window(expenses_data):
    expenses_history_window = CTkToplevel()
    expenses_history_window.title("Expenses History")
    expenses_history_window.geometry("800x600")

    
    #Month Label
    month_label = CTkLabel(expenses_history_window, text="Select Month:")
    month_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")

    #Dropdown menu for month
    month_dropdown = CTkOptionMenu(expenses_history_window, values=month)
    month_dropdown.grid(row=0, column=1, padx=10, pady=5, sticky=N)


    expenses_treeview = ttk.Treeview(expenses_history_window, columns=("Date", "Amount", "Category", "Note"), show="headings")
    expenses_treeview.heading("Date", text="Date")
    expenses_treeview.heading("Amount", text="Amount")
    expenses_treeview.heading("Category", text="Category")
    expenses_treeview.heading("Note", text="Note")
    expenses_treeview.grid(row=1, column=0, columnspan=2, padx=10, pady=5)

    #Insert expenses data into treeview
    for expense in expenses_data:
        expenses_treeview.insert("", "end", values=expense)