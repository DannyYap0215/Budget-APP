from customtkinter import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib import pyplot as plt
from collections import defaultdict
import tkinter.messagebox
import database_test as db
import sqlite3
# from set_income import income_data

def show_details(income_data):
    
    # Create a string to store the details
    details_text = "Income Details:\n\n"

    #danny's part
    con = sqlite3.connect("database.db")
    c = con.cursor()
    
    c.execute(f"SELECT months , allocated_income FROM allocated_income_for_month_2024")
    months_and_allocated_income = c.fetchall()
    rows = months_and_allocated_income
    
    
    # Append each income detail to the string
    for income in rows:
        month = income[0]  # Assuming month is at index 0
        amount = income[1]  # Assuming amount is at index 1
        details_text += f"Month: {month}\nAmount: {amount}\n\n"

    # Display the details in a message box
    tkinter.messagebox.showinfo("Income Details", details_text)

def open_income_piechart_window(income_data):
    con = sqlite3.connect("database.db")
    c = con.cursor()
    c.execute(f"SELECT months , allocated_income FROM allocated_income_for_month_2024")
    months_and_allocated_income = c.fetchall()
    rows = months_and_allocated_income
    
    
    # Filter out None values from income_data
    income_data_filtered = [(month, amount) for month, amount in income_data if amount is not None and amount.strip() != ""]

    income_piechart_window = CTk()
    income_piechart_window.title("Income Pie Chart")
    income_piechart_window.geometry("520x520+300+200")

    # Initialize a dictionary to store total income for each category
    month_income = defaultdict(float)

    # Calculate total income for each category
    for income in rows:
        month = income[0]  # Assuming month is at index 0
        amount = float(income[1])    # Assuming amount is at index 1
        month_income[month] += amount

    # Extract months and corresponding income
    income_months = list(month_income.keys())
    amounts = list(month_income.values())

     # Pie chart colors
    colours = ["#ffcd8e", "#ffb255", "#ff8ca1", "#f45f74", "#ffc9ed", "#b77ea3", "#8fd7d7", "#00b0be", "#bdd373", "#98c127"]

    fig = plt.figure()
    ax = fig.add_axes([0,0,1,1])
    ax.pie(amounts, labels = income_months , autopct='%1.2f%%',colors=colours)

    # Create a canvas widget for displaying the pie chart
    canvasbar = FigureCanvasTkAgg(fig, master=income_piechart_window)
    canvasbar.draw()
    canvasbar.get_tk_widget().place(relx=0.5, rely=0.5, anchor=CENTER)  

    # Create a Button widget to show more details
    details_button = CTkButton(income_piechart_window, text="Show Details", command=lambda: show_details(income_data_filtered))
    details_button.place(relx=0.5, rely=0.95, anchor="center")

    income_piechart_window.mainloop() 