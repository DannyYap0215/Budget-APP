from customtkinter import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib import pyplot as plt
from collections import defaultdict
import tkinter.messagebox
import database_test as db
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

def get_distinct_years():
    con = sqlite3.connect("database.db")
    c = con.cursor()
    c.execute("SELECT DISTINCT year FROM daily_expenses")
    years = c.fetchall()
    years = [str(year[0]) for year in years]
    con.close()
    return years

def show_details(selected_month):
    con = sqlite3.connect("database.db")
    c = con.cursor()
     # Filter expenses data by the selected month
    # filtered_expenses = [expense for expense in expenses_data if expense[0].strftime("%B") == selected_month]
    
    # Sort the filtered expenses data by date
    # filtered_expenses.sort(key=lambda x: x[0])  # Assuming date is at index 0
    
    # Create a string to store the sorted details
    details_text = f"Expense Details for {selected_month} :\n\n"

    c.execute("SELECT de.date, de.expenses, cd.category, de.note FROM daily_expenses de JOIN category_data cd ON de.cat_ID = cd.cat_ID WHERE de.months = ? AND year = ?", (selected_month,selected_year))
    rows = c.fetchall()

    # Append each expense detail to the string
    for expense in rows:
        date = expense[0]  # Assuming date is at index 0
        amount = expense[1]  # Assuming amount is at index 1
        category = expense[2]  # Assuming category is at index 2
        note = expense[3]  # Assuming note is at index 3
        details_text += f"Date: {date}\nAmount: {amount}\nCategory: {category}\nNote: {note}\n\n"

    # Create a root window (if not already created)
    root = CTk()
    root.withdraw()  # Hide the root window

    # Create a new top-level window to ensure the message box is on top
    top = CTkToplevel(root)
    top.attributes('-topmost', True)
    top.withdraw()  # Hide the top-level window

    # Display the details in a message box
    tkinter.messagebox.showinfo("Expenses Details", details_text, parent=top)

    # Destroy the top-level window after use
    top.destroy()
    root.destroy()

def open_expenses_piechart_window():
    expenses_piechart_window = CTkToplevel()
    expenses_piechart_window.title("Expenses Pie Chart")
    expenses_piechart_window.geometry("640x640+300+200")
    expenses_piechart_window.wm_attributes("-topmost",True)

    # Define the colors dictionary
    colors = {
    "red":"#FF5733",  # Red (Lighter shade)
    "green":"#4CAF50",  # Green (Darker shade)
    "blue":"#2196F3",  # Blue (Darker shade)
    "yellow":"#FFEB3B",  # Yellow (Darker shade)
    "orange":"#FF9800",  # Orange (Darker shade)
    "purple":"#9C27B0",  # Purple (Darker shade)
    "pink":"#E91E63",  # Pink (Darker shade)
    "brown":"#795548",  # Brown (Darker shade)
    "cyan":"#00BCD4",  # Cyan (Darker shade)
    "magenta":"#E040FB",  # Magenta (Darker shade)
    "black":"#212121",  # Black (Darker shade)
    "white":"#FFFFFF",  # White (Pure white)
    "gray":"#9E9E9E",  # Gray (Darker shade)
    "lightgray":"#BDBDBD",  # Lightgray (Lighter shade)
    "darkgray":"#616161",  # Darkgray (Darker shade)
    "lightblue":"#03A9F4",  # Lightblue (Lighter shade)
    "darkblue":"#1976D2",  # Darkblue (Darker shade)
    "lightgreen":"#8BC34A",  # Lightgreen (Lighter shade)
    "darkgreen":"#388E3C",  # Darkgreen (Darker shade)
    "lightred":"#FFCDD2",  # Lightred (Lighter shade)
    "darkred":"#D32F2F",  # Darkred (Darker shade)
    "lightyellow":"#FFF9C4",  # Lightyellow (Lighter shade)
    "darkyellow":"#FBC02D",  # Darkyellow (Darker shade)
    "lightorange":"#FFCC80",  # Lightorange (Lighter shade)
    "darkorange":"#FF5722",  # Darkorange (Darker shade)
    "lightpurple":"#CE93D8",  # Lightpurple (Lighter shade)
    "darkpurple":"#7B1FA2"   # Darkpurple (Darker shade)
}

    #Label for Expenses Pie Chart
    expenses_piechart_title_label = CTkLabel(expenses_piechart_window, text="Expenses Pie Chart", font=("Poppins-ExtraBold",30), text_color="#6965A3")
    expenses_piechart_title_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")

    # Year Label
    year_label = CTkLabel(expenses_piechart_window, text="Select Year:", font=("Poppins-ExtraBold", 20))
    year_label.grid(row=2, column=0, padx=10, pady=5, sticky="w")

    # Fetch distinct years from the database
    year_list = get_distinct_years()

    # Dropdown menu for year
    
    year_var = StringVar()
    year_dropdown = CTkOptionMenu(expenses_piechart_window, values=year_list, variable=year_var, fg_color="#6965A3")
    year_dropdown.grid(row=2, column=1, padx=10, pady=5, sticky=N)

    #Month Label
    month_label = CTkLabel(expenses_piechart_window, text="Select Month:", font=("Poppins-ExtraBold",20))
    month_label.grid(row=3, column=0, padx=10, pady=5, sticky="w")

    # month_set = set (expense[0].strftime("%B") for expense in expenses_data) #Extract month from the date entered
    # month_list = sorted (month_set) #Sort the extracted month

    #Dropdown menu for month
    month_var = StringVar()
    month_dropdown = CTkOptionMenu(expenses_piechart_window, values=months, variable=month_var, fg_color="#6965A3") 
    month_dropdown.grid(row=3, column=1, padx=10, pady=5, sticky=N)

    def update_expenses_piechart():
        global selected_year
        con = sqlite3.connect("database.db")
        c = con.cursor()
        selected_month = month_var.get()  # Get the selected month
        selected_year = year_var.get()  # Get the selected year

        # Filter expenses data by the selected month
        # filtered_expenses = [expense for expense in expenses_data if expense[0].strftime("%B") == selected_month]
        
        # # Initialize a dictionary to store total expenses for each category
        category_expenses = defaultdict(float)
        category_colors = {}

        # Calculate total expenses for each category
        c.execute("SELECT de.date, de.expenses, cd.category, cd.colour FROM daily_expenses de JOIN category_data cd ON de.cat_ID = cd.cat_ID WHERE de.months = ? AND year =?", (selected_month,year_dropdown.get()))
        rows = c.fetchall()

        for expense in rows:
            category = expense[2]  # Assuming category is at index 2
            amount = float(expense[1])    # Assuming amount is at index 1
            color_name = expense[3]  # Assuming color name is at index 3 in the database
            hex_color = colors.get(color_name)  # Retrieve hex color code from the predefined colors dictionary
            category_expenses[category] += amount
            category_colors[category] = hex_color
        
            if hex_color:
                # Color exists in the predefined colors dictionary
                print(f"Category: {category}, Hex Color: {hex_color}")
            else:
                # Color does not exist in the predefined colors dictionary
                print(f"Category: {category}, Color '{color_name}' not found in predefined colors.")

        # Extract categories and corresponding expenses
        expenses_categories = list(category_expenses.keys())
        weights = list(category_expenses.values())
        colours = [category_colors[category] for category in expenses_categories]

        fig = plt.figure()
        ax = fig.add_axes([0,0,1,1])
        ax.pie(weights, labels = expenses_categories , autopct='%1.2f%%',colors=colours)

        # Create a canvas widget for displaying the pie chart
        canvasbar = FigureCanvasTkAgg(fig, master=expenses_piechart_window)
        canvasbar.draw()
        canvasbar.get_tk_widget().place(relx=0.5, rely=0.55, anchor=CENTER)  

        # Create a Button widget to show more details
        details_button = CTkButton(expenses_piechart_window, text="Show Details", command=lambda: show_details(rows, selected_month))
        details_button.place(relx=0.5, rely=0.95, anchor="center")

    #Button to update expenses piechart
    update_button = CTkButton(expenses_piechart_window, text="Update", font=("Poppins-ExtraBold",15), fg_color="#6965A3", hover_color="#8885B6", command=update_expenses_piechart)
    update_button.grid(row=3, column=4, padx=10, pady=5, sticky="w")