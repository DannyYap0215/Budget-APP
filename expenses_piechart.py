from customtkinter import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib import pyplot as plt
from collections import defaultdict
import database_test as db
from datetime import datetime
import sqlite3
from PIL import Image

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

selected_icon = Image.open("icon/selected.png")

def get_distinct_years():
    con = sqlite3.connect("database.db")
    c = con.cursor()
    c.execute("SELECT DISTINCT year FROM daily_expenses")
    years = c.fetchall()
    years = [str(year[0]) for year in years]
    con.close()
    return years

def show_details_window(selected_month, selected_year):
    details_window = CTkToplevel()
    details_window.title("Expenses Details")
    details_window.geometry("800x600")
    details_window.wm_attributes("-topmost",True)

    # Add a label for the selected month and year
    month_year_label = CTkLabel(details_window, text=f"Expenses Details for {selected_month} {selected_year}", font=("Poppins-Bold", 30), text_color="#6965A3")
    month_year_label.pack(pady=15)

    con = sqlite3.connect("database.db")
    c = con.cursor()
    c.execute("SELECT de.date, de.expenses, cd.category FROM daily_expenses de JOIN category_data cd ON de.cat_ID = cd.cat_ID WHERE de.months = ? AND year = ? ORDER BY de.cat_ID", (selected_month, selected_year))
    rows = c.fetchall()

    # Initialize dictionaries to store statistics
    category_totals = defaultdict(float)
    category_counts = defaultdict(int)

    # Collect statistics
    for expense in rows:
        amount = expense[1]
        category = expense[2]

        # Update the totals and counts
        category_totals[category] += amount
        category_counts[category] += 1
    
    total_expenses = sum(category_totals.values())
    total_label = CTkLabel(details_window, text=f"Total Expenses: RM {total_expenses:.2f}", font=("Poppins-Bold", 25))
    total_label.pack(pady=(0, 10))

    # Create a frame to hold the details
    details_frame = CTkFrame(details_window)
    details_frame.pack(padx=20, pady=20, fill="both", expand=True)

    # Configure row and column weights
    for i in range(11):  # Assuming 11 rows and 4 columns in the table
        details_frame.grid_rowconfigure(i, weight=1)
    for j in range(4):
        details_frame.grid_columnconfigure(j, weight=1)

    # Create headers for the table
    headers = ["Category", "Total Expenses (RM)", "Number of Transactions", "Average Expenses (RM)"]
    for col, header in enumerate(headers):
        header_frame = CTkFrame(details_frame, border_width=1, corner_radius=0)
        header_frame.grid(row=0, column=col, sticky="nsew")
        header_label = CTkLabel(details_frame, text=header, font=("Poppins-Bold", 14))
        header_label.grid(row=0, column=col, padx=5, pady=5, sticky="nsew")
        
    # Insert data into the table
    for row, category in enumerate(category_totals.keys(), start=1):
        total = category_totals[category]
        count = category_counts[category]
        average = total / count

        for col, data in enumerate([category, f"{total:.2f}", f"{count}", f"{average:.2f}"]):
            data_frame = CTkFrame(details_frame, border_width=1, corner_radius=0)
            data_frame.grid(row=row, column=col, sticky="nsew")
            data_label = CTkLabel(details_frame, text=data, font=("Poppins", 12))
            data_label.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")

    con.close()

# Mei Ting part clear frame b4 open new one
def clear_frame(frame):
    for widget in frame.winfo_children():
        widget.destroy()

def open_expenses_piechart_window(expenses_piechart_frame):
    clear_frame(expenses_piechart_frame)

    # expenses_piechart_window = CTkToplevel()
    # expenses_piechart_window.title("Expenses Pie Chart")
    # expenses_piechart_window.geometry("640x640+300+200")
    # expenses_piechart_window.wm_attributes("-topmost",True)

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
    expenses_piechart_title_label = CTkLabel(expenses_piechart_frame, text="Expenses Pie Chart", font=CTkFont("font/Poppins-Bold.ttf",50,"bold"), text_color="#6965A3")
    expenses_piechart_title_label.place(relx=0.05, rely=0.08, anchor="w")

    # Year Label
    year_label = CTkLabel(expenses_piechart_frame, text="Select Year:", font=CTkFont("font/Poppins-Bold.ttf",35))
    year_label.place(relx=0.08, rely=0.18, anchor="w")
    year_selection_icon = CTkLabel(expenses_piechart_frame, text="", image= CTkImage(selected_icon))
    year_selection_icon.place(relx=0.05, rely=0.18, anchor="w")

    # Fetch distinct years from the database
    year_list = get_distinct_years()

    custom_font = CTkFont("font/Poppins-Bold.ttf", size=30)

    # Dropdown menu for year
    year_var = StringVar()
    year_dropdown = CTkOptionMenu(expenses_piechart_frame, values=year_list, variable=year_var, font=custom_font, fg_color="#6965A3", button_color="#3F3D65", button_hover_color="#A7A5C9")
    year_dropdown.place(relx=0.35, rely=0.18, anchor="w")

    #Month Label
    month_label = CTkLabel(expenses_piechart_frame, text="Select Month:", font=CTkFont("font/Poppins-Bold.ttf",35))
    month_label.place(relx=0.08, rely=0.26, anchor="w")
    month_selection_icon = CTkLabel(expenses_piechart_frame, text="", image= CTkImage(selected_icon))
    month_selection_icon.place(relx=0.05, rely=0.26, anchor="w")

    # month_set = set (expense[0].strftime("%B") for expense in expenses_data) #Extract month from the date entered
    # month_list = sorted (month_set) #Sort the extracted month

    #Dropdown menu for month
    month_var = StringVar()
    month_dropdown = CTkOptionMenu(expenses_piechart_frame, values=months, variable=month_var, font=custom_font, fg_color="#6965A3", button_color="#3F3D65", button_hover_color="#A7A5C9") 
    month_dropdown.place(relx=0.35, rely=0.26, anchor="w")

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
        c.execute("SELECT de.date, de.expenses, cd.category, cd.colour , de.note FROM daily_expenses de JOIN category_data cd ON de.cat_ID = cd.cat_ID WHERE de.months = ? AND year =?", (selected_month,year_dropdown.get()))
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
        canvasbar = FigureCanvasTkAgg(fig, master=expenses_piechart_frame)
        canvasbar.draw()
        canvasbar.get_tk_widget().place(relx=0.33, rely=0.63, anchor=CENTER)  

        # Create a Button widget to show more details
        details_button = CTkButton(expenses_piechart_frame, text="Show Details", font=CTkFont("font/Poppins-Bold.ttf",30), fg_color="#6965A3", hover_color="#8885B6", command=lambda: show_details_window(selected_month, selected_year))
        details_button.place(relx=0.33, rely=0.90, anchor="center")

    #Button to update expenses piechart
    update_button = CTkButton(expenses_piechart_frame, text="Update", font=CTkFont("font/Poppins-Bold.ttf",30), fg_color="#6965A3", hover_color="#8885B6", command=update_expenses_piechart)
    update_button.place(relx=0.35, rely=0.34, anchor="w")