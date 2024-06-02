import tkinter as tk
from customtkinter import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import mplcursors
import numpy as np
from collections import defaultdict
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

def parse_date(date):
    if isinstance(date, str):
        return datetime.strptime(date, "%d-%m-%Y")  # Adjust the format string as needed
    return date

# Mei Ting part clear frame b4 open new one
def clear_frame(frame):
    for widget in frame.winfo_children():
        widget.destroy()

def open_usage_barchart_window(usage_barchart_frame):
    clear_frame(usage_barchart_frame)

    # usage_barchart_window = CTk()
    # usage_barchart_window.title("Usage of Budget Bar Chart")
    # usage_barchart_window.geometry("800x600+300+200")
    # usage_barchart_window.wm_attributes("-topmost", True)

    # Label for Update Expenses
    usage_barchart_title_label = CTkLabel(usage_barchart_frame, text="Usage of Budget Bar Chart", font=CTkFont("font/Poppins-Bold.ttf",50,"bold"), text_color="#6965A3")
    usage_barchart_title_label.place(relx=0.05, rely=0.08, anchor="w")

    # Year Label
    year_label = CTkLabel(usage_barchart_frame, text="Select Year:", font=CTkFont("font/Poppins-Bold.ttf",35))
    year_label.place(relx=0.08, rely=0.18, anchor="w")
    year_selection_icon = CTkLabel(usage_barchart_frame, text="", image= CTkImage(selected_icon))
    year_selection_icon.place(relx=0.05, rely=0.18, anchor="w")

    con = sqlite3.connect("database.db")
    c = con.cursor()
    c.execute("SELECT DISTINCT year FROM budget_2024")
    years = c.fetchall()
    years = [str(year[0]) for year in years]

    custom_font = CTkFont("font/Poppins-Bold.ttf", size=30)

    # Dropdown menu for year
    year_var = tk.StringVar()
    year_dropdown = CTkOptionMenu(usage_barchart_frame, values=years, variable=year_var, font=custom_font, fg_color="#6965A3", button_color="#3F3D65", button_hover_color="#A7A5C9")
    year_dropdown.place(relx=0.35, rely=0.18, anchor="w")

    # Month Label
    month_label = CTkLabel(usage_barchart_frame, text="Select Month:", font=CTkFont("font/Poppins-Bold.ttf",35))
    month_label.place(relx=0.08, rely=0.26, anchor="w")
    month_selection_icon = CTkLabel(usage_barchart_frame, text="", image= CTkImage(selected_icon))
    month_selection_icon.place(relx=0.05, rely=0.26, anchor="w")

    # month_set = set(expense[0].strftime("%B") for expense in expenses_data)  # Extract month from the date entered
    # month_list = sorted(month_set)  # Sort the extracted month

    # Dropdown menu for month
    month_var = tk.StringVar()
    month_dropdown = CTkOptionMenu(usage_barchart_frame, values=months, variable=month_var, font=custom_font, fg_color="#6965A3", button_color="#3F3D65", button_hover_color="#A7A5C9")
    month_dropdown.place(relx=0.35, rely=0.26, anchor="w")

    def get_global_limits():
        min_value, max_value = 0, float('-inf')
        con = sqlite3.connect("database.db")
        c = con.cursor()
        for month in months:
            c.execute("SELECT bu.budget_allocated, bu.budget_used FROM budget_2024 bu WHERE bu.months = ?", (month,))
            rows = c.fetchall()
            if not rows:
                continue
            month_expenses = [float(row[1]) for row in rows]
            month_budget = [float(row[0]) for row in rows]
            all_values = month_expenses + month_budget
            max_value = max(max_value, max(all_values))
        con.close()
        range_buffer = max_value * 0.1  # Add a 10% buffer to the range
        return 0, max_value + range_buffer

    global_y_min, global_y_max = get_global_limits()

    def update_usage_barchart():
        selected_month = month_var.get()  # Get the selected month
        selected_year = year_var.get()  # Get the selected year
        con = sqlite3.connect("database.db")
        c = con.cursor()
        c.execute("SELECT cd.category, bu.months, bu.budget_allocated, bu.budget_used FROM budget_2024 bu JOIN category_data cd ON bu.cat_ID = cd.cat_ID WHERE bu.months = ? AND bu.year = ?", (selected_month, selected_year))
        rows = c.fetchall()
        print(rows)

        # Initialize dictionaries to store budget and expenses for each category
        budget_dict = defaultdict(float)
        expenses_dict = defaultdict(float)

        # Populate budget dictionary
        for row in rows:
            category = row[0]
            budget_amount = row[2]
            budget_dict[category] = float(budget_amount)

        # Populate expenses dictionary
        for row in rows:
            category = row[0]
            amount = row[3]
            expenses_dict[category] += float(amount)

        # Extract categories and corresponding budget and expenses
        categories_list = list(budget_dict.keys())
        budget_values = [budget_dict[category] for category in categories_list]
        expenses_values = [expenses_dict.get(category, 0) for category in categories_list]

        # Create a figure for the bar chart
        fig, ax1 = plt.subplots(figsize=(8, 5))

        # Create the bar chart
        bars = ax1.bar(categories_list, expenses_values, color='#00b0be', alpha=0.6, label='Expenses')
        ax1.set_xlabel('Categories')
        ax1.set_ylabel('Expenses', color='#00b0be')
        ax1.tick_params(axis='y', labelcolor='#00b0be')

        # Set the same limits and ticks for both y-axes
        ax1.set_ylim(global_y_min, global_y_max)

        # Annotate bar chart with expenses values
        for bar in bars:
            height = bar.get_height()
            ax1.annotate(f'RM {height}',
                         xy=(bar.get_x() + bar.get_width() / 2, height),
                         xytext=(0, 3),  # 3 points vertical offset
                         textcoords="offset points",
                         ha='center', va='bottom', fontsize=8, color='#00b0be')

        # Create the line chart with a secondary y-axis
        ax2 = ax1.twinx()
        line = ax2.plot(categories_list, budget_values, color='#f45f74', marker='o', label='Budget')[0]
        markers = ax2.scatter(categories_list, budget_values, color='#f45f74')
        ax2.set_ylabel('Budget', color='#f45f74')
        ax2.tick_params(axis='y', labelcolor='#f45f74')

        # Set the same limits and ticks for both y-axes
        ax2.set_ylim(global_y_min, global_y_max)

        # Add a legend
        lines, labels = ax1.get_legend_handles_labels()
        lines2, labels2 = ax2.get_legend_handles_labels()
        ax1.legend(lines + lines2, labels + labels2, loc='upper right')

        # Create a canvas to display the plot
        canvas = FigureCanvasTkAgg(fig, master=usage_barchart_frame)
        canvas.draw()
        canvas.get_tk_widget().place(relx=0.40, rely=0.63, anchor=tk.CENTER)

        # Add hover annotations using mplcursors
        cursor = mplcursors.cursor(markers, hover=True)
        @cursor.connect("add")
        def on_add(sel):
            sel.annotation.set_text(f'Budget: RM {sel.target[1]:.2f}')
            sel.annotation.get_bbox_patch().set_facecolor('#FF8CA1')  # Change background color
            sel.annotation.get_bbox_patch().set_edgecolor('#F45F74')  # Change edge color

    # Button to update usage barchart
    update_button = CTkButton(usage_barchart_frame, text="Update", font=CTkFont("font/Poppins-Bold.ttf",30), fg_color="#6965A3", hover_color="#8885B6", command=lambda: (update_usage_barchart(), reminder()))
    update_button.place(relx=0.35, rely=0.34, anchor="w")

    # Mei Ting part Reminder
    def reminder():
        reminder_frame = CTkFrame(usage_barchart_frame, width=360, height=215,
                              fg_color="#1f2124",border_color="#535085",
                              border_width=4,corner_radius=8)
        reminder_frame. place(relx=0.58, rely=0.26, anchor="w")
        reminder_title_label = CTkLabel(reminder_frame, text="Reminder",font=CTkFont("font/Poppins-Bold.ttf",28,"bold"))
        reminder_title_label.place(x=25, rely=0.18, anchor="w")
        reminder_textbox = CTkTextbox(reminder_frame, width=320, height=140, font=CTkFont("font/Poppins-Bold.ttf",25))
        reminder_textbox.place(x=20, rely=0.58, anchor="w")
        reminder_textbox.insert("1.0","Please hover your              cursor over the <red dots> on the graph to view            budget details.") #dont edit this line of code, the spaces in between words are for the text box display purpose    

    # usage_barchart_window.mainloop()
