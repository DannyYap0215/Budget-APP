from customtkinter import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib import pyplot as plt
from collections import defaultdict
import tkinter.messagebox
import database_test as db

def show_details(expenses_data):
    # Create a string to store the details
    details_text = "Expense Details:\n\n"

    # Append each expense detail to the string
    for expense in expenses_data:
        date = expense[0]  # Assuming date is at index 0
        amount = expense[1]  # Assuming amount is at index 1
        category = expense[2]  # Assuming category is at index 2
        note = expense[3]  # Assuming note is at index 3
        details_text += f"Date: {date}\nAmount: {amount}\nCategory: {category}\nNote: {note}\n\n"

    # Display the details in a message box
    tkinter.messagebox.showinfo("Expense Details", details_text)

def open_expenses_piechart_window(expenses_data):
    expenses_piechart_window = CTk()
    expenses_piechart_window.title("Expenses Pie Chart")
    expenses_piechart_window.geometry("520x520+300+200")

    # Initialize a dictionary to store total expenses for each category
    category_expenses = defaultdict(float)

    # Calculate total expenses for each category
    for expense in expenses_data:
        category = expense[2]  # Assuming category is at index 2
        amount = float(expense[1])    # Assuming amount is at index 1
        category_expenses[category] += amount

    # Extract categories and corresponding expenses
    expenses_categories = list(category_expenses.keys())
    weights = list(category_expenses.values())

     # Pie chart colors
    colours = ["#ffcd8e", "#ffb255", "#ff8ca1", "#f45f74", "#ffc9ed", "#b77ea3", "#8fd7d7", "#00b0be", "#bdd373", "#98c127"]

    fig = plt.figure()
    ax = fig.add_axes([0,0,1,1])
    ax.pie(weights, labels = expenses_categories , autopct='%1.2f%%',colors=colours)

    # Create a canvas widget for displaying the pie chart
    canvasbar = FigureCanvasTkAgg(fig, master=expenses_piechart_window)
    canvasbar.draw()
    canvasbar.get_tk_widget().place(relx=0.5, rely=0.5, anchor=CENTER)  

    # Create a Button widget to show more details
    details_button = CTkButton(expenses_piechart_window, text="Show Details", command=lambda: show_details(expenses_data))
    details_button.place(relx=0.5, rely=0.95, anchor="center")

    expenses_piechart_window.mainloop() 