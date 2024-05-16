from customtkinter import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import numpy as np
from collections import defaultdict
from datetime import datetime
import sqlite3

months = [
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

def parse_date(date):
    if isinstance(date, str):
        return datetime.strptime(date, "%d-%m-%Y")  # Adjust the format string as needed
    return date

# Ensure all dates in expenses_data are datetime objects
# expenses_data = [(parse_date(expense[0]), expense[1], expense[2], expense[3]) for expense in expenses_data]

def open_usage_barchart_window(budget_data, expenses_data):
    usage_barchart_window = CTk()
    usage_barchart_window.title("Usage of Budget Bar Chart")
    usage_barchart_window.geometry("720x720+300+200")
    usage_barchart_window.wm_attributes("-topmost",True)

    #Label for Update Expenses
    usage_barchart_title_label = CTkLabel(usage_barchart_window, text="Usage of Budget Bar Chart", font=("Poppins-ExtraBold",30), text_color="#6965A3")
    usage_barchart_title_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")

    #Month Label
    month_label = CTkLabel(usage_barchart_window, text="Select Month:", font=("Poppins-ExtraBold",20))
    month_label.grid(row=3, column=0, padx=10, pady=5, sticky="w")

    month_set = set (expense[0].strftime("%B") for expense in expenses_data) #Extract month from the date entered
    month_list = sorted (month_set) #Sort the extracted month

    #Dropdown menu for month
    month_var = StringVar()
    month_dropdown = CTkOptionMenu(usage_barchart_window, values=months, variable=month_var, fg_color="#6965A3") 
    month_dropdown.grid(row=3, column=1, padx=10, pady=5, sticky=N)

    def update_usage_barchart():
        selected_month = month_var.get()  # Get the selected month
        con = sqlite3.connect("database.db")
        c = con.cursor()
        c.execute("SELECT cd.category, bu.months, bu.budget_allocated, bu.budget_used FROM budget_2024 bu JOIN category_data cd ON bu.cat_ID = cd.cat_ID WHERE bu.months = ?", (selected_month,))
        rows = c.fetchall()
        print(rows)
        # Filter expenses data by the selected month
        # filtered_expenses = [expense for expense in expenses_data if expense[0].strftime("%B") == selected_month]

        # Initialize dictionaries to store budget and expenses for each category
        budget_dict = defaultdict(float)
        expenses_dict = defaultdict(float)

        # # Populate budget dictionary
        # for category, budget_amount in zip(rows[0], rows[2]):
        #     budget_dict[category] = float(budget_amount)

        # # Populate expenses dictionary
        # for row in rows:
        #     category, amount = row[0], row[3]
        #     expenses_dict[category] += float(amount)
        
        
        # Populate expenses dictionary
        # Populate budget dictionary
        for row in rows:
            category = row[0]
            budget_amount = row[2]
            budget_dict[category] = float(budget_amount)

        for row in rows:
            category = row[0]
            amount = row[3]
            expenses_dict[category] += float(amount)

        # Extract categories and corresponding budget and expenses
        categories_list = list(budget_dict.keys())
        budget_values = [budget_dict[category] for category in categories_list]
        expenses_values = [expenses_dict.get(category, 0) for category in categories_list]

        # Bar chart settings
        bar_width = 0.35
        index = np.arange(len(categories_list))

        # Create a figure for the bar chart
        fig, ax = plt.subplots()
        ax.bar(index, budget_values, bar_width, label='Budget', color = "#bdd373")
        ax.bar(index, expenses_values, bar_width, label='Expenses', color = "#ff8ca1")

        ax.set_xlabel('Categories')
        ax.set_ylabel('Amount (RM)')
        ax.set_title('Usage of Budget')
        ax.set_xticks(index)
        ax.set_xticklabels(categories_list, rotation=45, ha='right')
        ax.legend()

        plt.tight_layout()

        # Clear previous chart if exists
        for widget in usage_barchart_window.winfo_children():
            if isinstance(widget, FigureCanvasTkAgg):
                widget.get_tk_widget().destroy()
        
        # Create a canvas widget for displaying the bar chart
        canvasbar = FigureCanvasTkAgg(fig, master=usage_barchart_window)
        canvasbar.draw()
        canvasbar.get_tk_widget().place(relx=0.5, rely=0.5, anchor=CENTER)  

     #Button to update usage barchart
    update_button = CTkButton(usage_barchart_window, text="Update", font=("Poppins-ExtraBold",15), fg_color="#6965A3", hover_color="#8885B6", command=update_usage_barchart)
    update_button.grid(row=3, column=4, padx=10, pady=5, sticky="w")

    usage_barchart_window.mainloop()