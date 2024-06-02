from customtkinter import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib import pyplot as plt
from collections import defaultdict
import database_test as db
import sqlite3
from PIL import Image
# from set_income import income_data

selected_icon = Image.open("icon/selected.png")

def show_details(year_selected):
    details_window = CTkToplevel()
    details_window.title("Income Details")
    details_window.geometry("800x600")
    details_window.wm_attributes("-topmost",True)

    # Add a label for the selected year
    year_label = CTkLabel(details_window, text=f"Income Details for {year_selected}", font=("Poppins-Bold", 30), text_color="#6965A3")
    year_label.pack(pady=15)

    con = sqlite3.connect("database.db")
    c = con.cursor()
    c.execute("SELECT months , allocated_income FROM allocated_income_for_month_2024 WHERE year = ?",(year_selected,))
    rows = c.fetchall()

    # Collect monthly income data
    month_income = {row[0]: row[1] for row in rows}

    total_income = sum(month_income.values())
    average_income = total_income / 12  # Calculate average income over 12 months
    
    total_label = CTkLabel(details_window, text=f"Total Income: RM {total_income:.2f}", font=("Poppins-Bold", 25))
    total_label.pack(pady=(0, 10))

    average_label = CTkLabel(details_window, text=f"Average Monthly Income: RM {average_income:.2f}", font=("Poppins-Bold", 25))
    average_label.pack(pady=(0, 10))

    # Create a frame to hold the details
    details_frame = CTkFrame(details_window)
    details_frame.pack(padx=20, pady=20, fill="both", expand=True)

    # Configure row and column weights
    for i in range(13):  # Assuming 13 rows and 2 columns in the table
        details_frame.grid_rowconfigure(i, weight=1)
    for j in range(2):
        details_frame.grid_columnconfigure(j, weight=1)

    # Create headers for the table
    headers = ["Month", "Total Income (RM)"]
    for col, header in enumerate(headers):
        header_frame = CTkFrame(details_frame, border_width=1, corner_radius=0)
        header_frame.grid(row=0, column=col, sticky="nsew")
        header_label = CTkLabel(details_frame, text=header, font=("Poppins-Bold", 14))
        header_label.grid(row=0, column=col, padx=5, pady=5, sticky="nsew")

    # Insert data into the table
    for row, (month, total) in enumerate(month_income.items(), start=1):
        data_frame_month = CTkFrame(details_frame, border_width=1, corner_radius=0)
        data_frame_month.grid(row=row, column=0, sticky="nsew")
        data_label_month = CTkLabel(data_frame_month, text=month, font=("Poppins", 12))
        data_label_month.pack(padx=5, pady=5, fill="both", expand=True)

        data_frame_total = CTkFrame(details_frame, border_width=1, corner_radius=0)
        data_frame_total.grid(row=row, column=1, sticky="nsew")
        data_label_total = CTkLabel(data_frame_total, text=f"{total:.2f}", font=("Poppins", 12))
        data_label_total.pack(padx=5, pady=5, fill="both", expand=True)

    con.close()

def clear_frame(frame):
    for widget in frame.winfo_children():
        widget.destroy()

def open_income_piechart_window(income_piechart_frame):
    clear_frame(income_piechart_frame)

    # income_piechart_window = CTk()
    # income_piechart_window.title("Income Pie Chart")
    # income_piechart_window.geometry("640x640+300+200")
    # income_piechart_window.wm_attributes("-topmost",True)

    #Label for Income Pie Chart
    income_piechart_title_label = CTkLabel(income_piechart_frame, text="Income Pie Chart", font=CTkFont("font/Poppins-Bold.ttf",50,"bold"), text_color="#6965A3")
    income_piechart_title_label.place(relx=0.05, rely=0.08, anchor="w")
    # Year Label
    year_label = CTkLabel(income_piechart_frame, text="Select Year:", font=CTkFont("font/Poppins-Bold.ttf",35))
    year_label.place(relx=0.08, rely=0.18, anchor="w")
    year_selection_icon = CTkLabel(income_piechart_frame, text="", image= CTkImage(selected_icon))
    year_selection_icon.place(relx=0.05, rely=0.18, anchor="w")

    con = sqlite3.connect("database.db")
    c = con.cursor()
    c.execute("SELECT DISTINCT year FROM allocated_income_for_month_2024")
    years = c.fetchall()
    years = [str(year[0]) for year in years]

    # Dropdown menu for year
    year_var = StringVar()
    year_dropdown = CTkOptionMenu(income_piechart_frame, values=years, variable=year_var, fg_color="#6965A3")
    year_dropdown.place(relx=0.35, rely=0.18, anchor="w")
   # year_var.set(years[0]) 
    
    def update_income_piechart():
        global year_selected
        year_selected = year_var.get()
        con = sqlite3.connect("database.db")
        c = con.cursor()
        c.execute(f"SELECT months , allocated_income FROM allocated_income_for_month_2024 WHERE year = ?",(year_selected,))
        months_and_allocated_income = c.fetchall()
        rows = months_and_allocated_income
        
        # Filter out None values from income_data
        # income_data_filtered = [(month, amount) for month, amount in income_data if amount is not None and amount.strip() != ""]

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
        canvasbar = FigureCanvasTkAgg(fig, master=income_piechart_frame)
        canvasbar.draw()
        canvasbar.get_tk_widget().place(relx=0.33, rely=0.45, anchor=CENTER)  

        # Create a Button widget to show more details
        details_button = CTkButton(income_piechart_frame, text="Show Details", font=CTkFont("font/Poppins-Bold.ttf",30), fg_color="#6965A3", hover_color="#8885B6", command=lambda: show_details(year_selected))
        details_button.place(relx=0.33, rely=0.73, anchor="center")

    #Button to update expenses piechart
    update_button = CTkButton(income_piechart_frame, text="Update", font=CTkFont("font/Poppins-Bold.ttf",30), fg_color="#6965A3", hover_color="#8885B6", command=update_income_piechart)
    update_button.place(relx=0.60, rely=0.18, anchor="w")

    # income_piechart_frame.mainloop()