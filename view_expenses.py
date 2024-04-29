from customtkinter import *
from tkcalendar import DateEntry
from tkinter import ttk

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

# Sample expenses data for demonstration
sample_expenses_data = [
    {"date": "01-01-2024", "category": "Food", "amount": 50.00, "note": "Lunch with friends"},
    {"date": "05-01-2024", "category": "Transport", "amount": 30.00, "note": "Taxi fare"},
    {"date": "10-01-2024", "category": "Household", "amount": 100.00, "note": "Groceries"},
    # Add more sample expenses data here if needed
]

def open_expenses_history_window():
    expense_history_window = CTkToplevel()
    expense_history_window.title("Expense History")
    expense_history_window.geometry("800x600")

    #Month Label
    month_label = CTkLabel(expense_history_window, text="Select Month:")
    month_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")

    #Dropdown menu for month
    month_dropdown = CTkOptionMenu(expense_history_window, values=month)
    month_dropdown.grid(row=0, column=1, padx=10, pady=5, sticky=N)
