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

    #DateEntry widget for selecting date
    date_entry = DateEntry(update_expenses_window, selectmode="day")
    date_entry.grid(row=1, column=1, padx=10, pady=5, sticky="w")

    # Function to update date and save as string
    def save_date():
        date = date_entry.get_date()
        date_string = date.strftime("%d-%m-%y")  #Format date as "dd-mm-yy"
        date_entry.delete(0, 'end')  #Clear text in the entry
        date_entry.insert(0, date_string)  #Insert selected date as text

    #Button to save date as text
    get_date_button = CTkButton(update_expenses_window, text="Get Date", command=save_date)
    get_date_button.grid(row=1, column=3, padx=10, pady=5, sticky="w")

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