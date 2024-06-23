import subprocess
import sys


def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])
    print(f"installing {package}")

try:
    import tkinter
except ImportError:
    install("tk")
    import tkinter

try:
    import customtkinter
except ImportError:
    install("customtkinter")
    import customtkinter

try:
    import matplotlib
except ImportError:
    install("matplotlib")
    import matplotlib

try:
    import pyparsing
except ImportError:
    install("pyparsing")
    import pyparsing

try:
    import tkcalendar
except ImportError:
    install("tkcalendar")
    import tkcalendar

        
from customtkinter import *
import tkinter as tk
from PIL import Image
from time import strftime
from datetime import datetime
import edit_budget
import update_expenses
import expenses_history
import expenses_piechart
import income_piechart
import insight
import settings




root = CTk()
root.title("Budget Dashboard")
screen_width = 1920
screen_height = 1080
root.geometry(f"{screen_width}x{screen_height}")

set_appearance_mode("dark")

def toggle_fullscreen(event=None):
    state = not root.attributes('-fullscreen') #True or False basically 
    root.attributes('-fullscreen', state)
    
insight_icon = Image.open("icon/insight.png")
edit_budget_icon = Image.open("icon/edit_budget.png")
update_expenses_icon = Image.open("icon/update_expenses.png")
expenses_history_icon = Image.open("icon/expenses_history.png")
settings_icon = Image.open("icon/settings.png")

def hide_indicator():
    insight_indicator.configure(fg_color="#535085", bg_color="#535085")
    edit_budget_indicator.configure(fg_color="#535085", bg_color="#535085")
    update_expenses_indicator.configure(fg_color="#535085", bg_color="#535085")
    expenses_history_indicator.configure(fg_color="#535085", bg_color="#535085")
    settings_indicator.configure(fg_color="#535085", bg_color="#535085")

def indicator(label):
    hide_indicator()
    label.configure(fg_color="#8885B6", bg_color="#535085")

def open_insight_window():
    insight.open_insight_window(dashboard_right_frame)

def open_edit_budget_window():
    edit_budget.open_edit_budget_window(dashboard_right_frame)

def open_update_expenses_window():
    update_expenses.open_update_expenses_window(dashboard_right_frame)

def open_expenses_history_window():
    expenses_history.open_expenses_history_window(dashboard_right_frame)

def open_settings_window():
    settings.Settings(dashboard_right_frame,root)
    

dashboard_left_frame = CTkFrame(master=root, width=420, height=1080, corner_radius=10, fg_color="#535085")
dashboard_left_frame.place(relx=0.0, rely=0.5, anchor="w")
    
insight_button = CTkButton(root, image=CTkImage(insight_icon), text="Insight", font=CTkFont("font/Poppins-Bold.ttf",35), 
                           corner_radius=10, fg_color="#8885B6", bg_color="#535085", hover_color="#2B2A45", text_color="#FFFFFF", 
                           command=lambda:(indicator(insight_indicator), open_insight_window()))
insight_button.place(relx=0.03, rely=0.22, anchor="w")
insight_indicator = CTkLabel(root, text="", width=8, height=45, bg_color="#535085")
insight_indicator.place(relx=0.02, rely=0.22, anchor="w")

edit_budget_button = CTkButton(root, image=CTkImage(edit_budget_icon), text="Edit Budget", font=CTkFont("font/Poppins-Bold.ttf",35), 
                               corner_radius=10, fg_color="#8885B6", bg_color="#535085", hover_color="#2B2A45", text_color="#FFFFFF", 
                               command=lambda:(indicator(edit_budget_indicator), open_edit_budget_window()))
edit_budget_button.place(relx=0.03, rely=0.32, anchor="w")
edit_budget_indicator = CTkLabel(root, text="", width=8, height=45, bg_color="#535085")
edit_budget_indicator.place(relx=0.02, rely=0.32, anchor="w")

update_expenses_button = CTkButton(root, image=CTkImage(update_expenses_icon), text="Update Expenses", font=CTkFont("font/Poppins-Bold.ttf",35), 
                                   corner_radius=10, fg_color="#8885B6", bg_color="#535085", hover_color="#2B2A45", text_color="#FFFFFF", 
                                   command=lambda:(indicator(update_expenses_indicator), open_update_expenses_window()))
update_expenses_button.place(relx=0.03, rely=0.42, anchor="w")
update_expenses_indicator = CTkLabel(root, text="", width=8, height=45, bg_color="#535085")
update_expenses_indicator.place(relx=0.02, rely=0.42, anchor="w")

expenses_history_button = CTkButton(root, image=CTkImage(expenses_history_icon), text="Expenses History", 
                                    font=CTkFont("font/Poppins-Bold.ttf",35), corner_radius=10, fg_color="#8885B6", bg_color="#535085", 
                                    hover_color="#2B2A45", text_color="#FFFFFF", 
                                    command=lambda:(indicator(expenses_history_indicator), open_expenses_history_window()))
expenses_history_button.place(relx=0.03, rely=0.52, anchor="w")
expenses_history_indicator = CTkLabel(root, text="", width=8, height=45, bg_color="#535085")
expenses_history_indicator.place(relx=0.02, rely=0.52, anchor="w")

settings_button = CTkButton(root, image=CTkImage(settings_icon), text="Settings", 
                                    font=CTkFont("font/Poppins-Bold.ttf",35), corner_radius=10, fg_color="#8885B6", bg_color="#535085", 
                                    hover_color="#2B2A45", text_color="#FFFFFF", 
                                    command=lambda:(indicator(settings_indicator), open_settings_window()))
settings_button.place(relx=0.03, rely=0.62, anchor="w")
settings_indicator = CTkLabel(root, text="", width=8, height=45, bg_color="#535085")
settings_indicator.place(relx=0.02, rely=0.62, anchor="w")

dashboard_right_frame = CTkFrame(master=root, width=1500, height=1080, corner_radius=10, fg_color="#202124")
dashboard_right_frame.place(relx=0.22, rely=0.5, anchor="w")

#Date function
def update_date():
    date_string = datetime.now().strftime("%d/%m/%Y")
    date_label.configure(text=date_string)

#Clock function
def clock_time ():
        clock_string = strftime("%H:%M:%S %p")
        clock_label.configure(text=clock_string)
        clock_label.after(1000, clock_time)

#Date Label
date_label = CTkLabel(root, font=CTkFont("Jersey.ttf", 30, "bold"), bg_color="#535085")
date_label.place(relx=0.062, rely=0.82, anchor="w")
update_date()

#Clock Label
clock_label = CTkLabel(root, font=CTkFont("Jersey.ttf", 30, "bold"), bg_color="#535085")
clock_label.place(relx=0.057, rely=0.87, anchor="w")
clock_time()

root.bind("<F11>", toggle_fullscreen)

root.mainloop()
