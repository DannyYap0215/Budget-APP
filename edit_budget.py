from customtkinter import *
import set_income
import set_categories
from PIL import Image

set_income_icon = Image.open("icon/update_expenses.png")
set_categories_icon = Image.open("icon/category_icon.png")

def open_set_income_window(budget_frame_two):
    set_income.open_set_income_window(budget_frame_two)
    
def open_set_categories_window(budget_frame_two):
    set_categories.open_set_categories_window(budget_frame_two)
    
def open_edit_budget_window(edit_budget_frame):
    for widget in edit_budget_frame.winfo_children():
        widget.destroy()

    # def on_button_click():
    #     # Reduce the topmost attribute when a button is clicked
    #     edit_budget_frame.wm_attributes("-topmost", False)
    
    budget_frame_two = CTkFrame(master=edit_budget_frame, width=1160, height=1080, corner_radius=10, border_width=2, border_color="#535085", fg_color="#202124")
    budget_frame_two.place(relx=0.23, rely=0.5, anchor="w")

    #Label for Update Expenses
    edit_budget_title_label = CTkLabel(edit_budget_frame, text="Edit Budget", 
                                           font=CTkFont("font/Poppins-Bold.ttf",50,"bold") , text_color="#6965A3")
    edit_budget_title_label.place(relx=0.02, rely=0.08, anchor="w")

    set_income_button = CTkButton(edit_budget_frame, text="Set Income", font=CTkFont("font/Poppins-Bold.ttf",30), 
                                fg_color="#6965A3", hover_color="#8885B6", image=CTkImage(set_income_icon), command=lambda:open_set_income_window(budget_frame_two))
    set_income_button.place(relx=0.02, rely=0.18, anchor="w")
    
    set_categories_button = CTkButton(edit_budget_frame, text="Set Categories", font=CTkFont("font/Poppins-Bold.ttf",30), 
                                fg_color="#6965A3", hover_color="#8885B6", image=CTkImage(set_categories_icon), command=lambda:open_set_categories_window(budget_frame_two))
    set_categories_button.place(relx=0.02, rely=0.28, anchor="w")
    
    # #check for m1 click on the button if so it goes through the function o_b_c()
    # set_income_button.bind("<Button-1>", lambda event: on_button_click())
    # set_categories_button.bind("<Button-1>", lambda event: on_button_click())
