from customtkinter import *
import tkinter as tk
from PIL import Image
import edit_budget
import update_expenses
import expenses_history
import expenses_piechart
import income_piechart
from update_expenses import expenses_data
from set_income import income_data
from set_categories import allocated
import insight


root = CTk()
root.title("Budget!")
screen_width = 1920
screen_height = 1080
root.geometry(f"{screen_width}x{screen_height}")

set_appearance_mode("dark")
insight_icon = Image.open("icon/insight.png")
edit_budget_icon = Image.open("icon/edit_budget.png")
update_expenses_icon = Image.open("icon/update_expenses.png")
expenses_history_icon = Image.open("icon/expenses_history.png")

dashboard_left_frame = CTkFrame(master=root, width=400, height=1080, corner_radius=10, fg_color="#535085")
dashboard_left_frame.place(relx=0.0, rely=0.5, anchor="w")

insight_button = CTkButton(root, image=CTkImage(insight_icon), text="Insight", font=CTkFont("font/Poppins-Bold.ttf",35), corner_radius=10, fg_color="#8885B6", bg_color="#535085", hover_color="#2B2A45", text_color="#FFFFFF")
insight_button.place(relx=0.02, rely=0.3, anchor="w")

edit_budget_button = CTkButton(root, image=CTkImage(edit_budget_icon), text="Edit Budget", font=CTkFont("font/Poppins-Bold.ttf",35), corner_radius=10, fg_color="#8885B6", bg_color="#535085", hover_color="#2B2A45", text_color="#FFFFFF")
edit_budget_button.place(relx=0.02, rely=0.4, anchor="w")

update_expenses_button = CTkButton(root, image=CTkImage(update_expenses_icon), text="Update Expenses", font=CTkFont("font/Poppins-Bold.ttf",35), corner_radius=10, fg_color="#8885B6", bg_color="#535085", hover_color="#2B2A45", text_color="#FFFFFF")
update_expenses_button.place(relx=0.02, rely=0.5, anchor="w")

expenses_history_button = CTkButton(root, image=CTkImage(expenses_history_icon), text="Expenses History", font=CTkFont("font/Poppins-Bold.ttf",35), corner_radius=10, fg_color="#8885B6", bg_color="#535085", hover_color="#2B2A45", text_color="#FFFFFF")
expenses_history_button.place(relx=0.02, rely=0.6, anchor="w")


# def toggle_fullscreen(event=None):
    # state = not root.attributes('-fullscreen') #True or False basically 
    # root.attributes('-fullscreen', state)
    
# def open_edit_budget_window():
#     edit_budget.open_edit_budget_window()
    
# def open_update_expenses_window():
#     update_expenses.open_update_expenses_window()

# def open_insight_window():
#     insight.open_insight_window(expenses_piechart, income_piechart, expenses_data, income_data, allocated)

# def open_expenses_history_window():
#     expenses_history.open_expenses_history_window(expenses_data)
    
# insight_button = CTkButton(root, text="Insight", height= 10,width=20, command=open_insight_window)
# insight_button.grid(row=0, column=1, padx=10, pady=5, sticky="w",)

# edit_budget_button = CTkButton(root, text="Edit Budget", height= 10,width=20, command=open_edit_budget_window)
# edit_budget_button.grid(row=1, column=1, padx=10, pady=5,sticky="w")

# update_expenses_button = CTkButton(root, text="Update Expenses",height= 10,width=20, command=open_update_expenses_window)
# update_expenses_button.grid(row=2, column=1, padx=10, pady=5, sticky="w")

# expenses_history_button = CTkButton(root, text="Expenses History",height= 10,width=20, command=open_expenses_history_window)
# expenses_history_button.grid(row=3, column=1, padx=10, pady=5, sticky="w")

# root.bind("<F11>", toggle_fullscreen)

root.mainloop()
