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
    
    c.execute(f"SELECT months , allocated_income FROM allocated_income_for_month_2024 WHERE year = ?",(year_selected,))
    months_and_allocated_income = c.fetchall()
    rows = months_and_allocated_income
    
    # Append each income detail to the string
    for income in rows:
        month = income[0]  # Assuming month is at index 0
        amount = income[1]  # Assuming amount is at index 1
        details_text += f"Month: {month}\nAmount: {amount}\n\n"

    # Create a root window (if not already created)
    root = CTk()
    root.withdraw()  # Hide the root window

    # Create a new top-level window to ensure the message box is on top
    top = CTkToplevel(root)
    top.attributes('-topmost', True)
    top.withdraw()  # Hide the top-level window

    # Display the details in a message box
    tkinter.messagebox.showinfo("Income Details", details_text, parent=top)

    # Destroy the top-level window after use
    top.destroy()
    root.destroy()

def open_income_piechart_window(income_data):
    income_piechart_window = CTk()
    income_piechart_window.title("Income Pie Chart")
    income_piechart_window.geometry("640x640+300+200")
    income_piechart_window.wm_attributes("-topmost",True)

    #Label for Income Pie Chart
    income_piechart_title_label = CTkLabel(income_piechart_window, text="Income Pie Chart", font=("Poppins-ExtraBold",30), text_color="#6965A3")
    income_piechart_title_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")

    # Year Label
    year_label = CTkLabel(income_piechart_window, text="Select Year:", font=("Poppins-ExtraBold", 20))
    year_label.grid(row=2, column=0, padx=10, pady=5, sticky="w")

    con = sqlite3.connect("database.db")
    c = con.cursor()
    c.execute("SELECT DISTINCT year FROM daily_expenses")
    years = c.fetchall()
    years = [str(year[0]) for year in years]

    # Dropdown menu for year
    year_var = StringVar()
    year_dropdown = CTkOptionMenu(income_piechart_window, values=years, variable=year_var, fg_color="#6965A3")
    year_dropdown.grid(row=2, column=1, padx=10, pady=5, sticky=N)
    year_var.set(years[0]) 
    


    def update_income_piechart():
        global year_selected
        year_selected = year_var.get()
        con = sqlite3.connect("database.db")
        c = con.cursor()
        c.execute(f"SELECT months , allocated_income FROM allocated_income_for_month_2024 WHERE year = ?",(year_selected,))
        months_and_allocated_income = c.fetchall()
        rows = months_and_allocated_income
        
        # Filter out None values from income_data
        income_data_filtered = [(month, amount) for month, amount in income_data if amount is not None and amount.strip() != ""]

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
        canvasbar.get_tk_widget().place(relx=0.5, rely=0.55, anchor=CENTER)  

        # Create a Button widget to show more details
        details_button = CTkButton(income_piechart_window, text="Show Details", command=lambda: show_details(income_data_filtered))
        details_button.place(relx=0.5, rely=0.95, anchor="center")

    #Button to update expenses piechart
    update_button = CTkButton(income_piechart_window, text="Update", font=("Poppins-ExtraBold",15), fg_color="#6965A3", hover_color="#8885B6", command=update_income_piechart)
    update_button.grid(row=2, column=4, padx=10, pady=5, sticky="w") 

    income_piechart_window.mainloop()