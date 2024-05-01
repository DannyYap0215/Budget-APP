from customtkinter import *
from tkcalendar import DateEntry
from datetime import datetime

expenses_categories = [
    "Food",
    "Transport",
    "Household",
    "Pets",
    "Apparel",
    "Beauty",
    "Health",
    "Education",
    "Social Life",
    "Gift",
]

expenses_data = []

def open_update_expenses_window():
    update_expenses_window = CTkToplevel()
    update_expenses_window.title("Update Expenses")
    update_expenses_window.geometry("500x400")
    
    #Label for date
    date_picker_label = CTkLabel(update_expenses_window, text="Date :")
    date_picker_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")

    def update_date_format(event):
        date_entry.set_date(date_entry.get_date().strftime("%d-%m-%Y"))
        
    #DateEntry widget for selecting date
    date_entry = DateEntry(update_expenses_window, selectmode="day", date_pattern="dd-mm-yyyy")
    date_entry.grid(row=1, column=1, padx=10, pady=5, sticky="w")
    date_entry.bind("<<DateEntrySelected>>", update_date_format)

    #Label for expenses amount
    expenses_amount_label = CTkLabel(update_expenses_window, text="Expenses : ")
    expenses_amount_label.grid(row=3, column=0, padx=10, pady=5, sticky="w")

    #Entry for expenses amount
    expenses_amount_entry = CTkEntry(update_expenses_window)
    expenses_amount_entry.grid(row=3, column=1, padx=10, pady=5, sticky="w")

    #Label for expenses category
    expenses_categories_label = CTkLabel(update_expenses_window, text="Category :")
    expenses_categories_label.grid(row=5, column=0, padx=10, pady=5, sticky="w")

    #dropdown expenses category menu
    expenses_categories_menu = CTkOptionMenu(update_expenses_window, values=expenses_categories)
    expenses_categories_menu.grid(row=5, column=1, padx=10, pady=5, sticky="w")

    #Label for note
    expenses_note_label = CTkLabel(update_expenses_window, text="Note :")
    expenses_note_label.grid(row=7, column=0, padx=10, pady=5, sticky="w")

    #Entry for note
    expenses_note_entry = CTkEntry(update_expenses_window)
    expenses_note_entry.grid(row=7, column=1, padx=10, pady=5, sticky="w")

    def save_expenses():
        expenses_date = date_entry.get_date()
        expenses_amount = expenses_amount_entry.get()
        expenses_categories = expenses_categories_menu.get()
        expenses_note = expenses_note_entry.get()
        expenses_data.append((expenses_date, expenses_amount, expenses_categories, expenses_note))
        update_expenses_window.destroy()
    
    #Button to save expenses
    save_expenses_button = CTkButton(update_expenses_window, text="Save Expenses", command=save_expenses)
    save_expenses_button.grid(row=9, column=0, padx=10, pady=5, sticky="w")