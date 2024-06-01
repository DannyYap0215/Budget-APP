from customtkinter import *
from tkcalendar import DateEntry
from datetime import datetime
from PIL import Image
import database_test as db

# expenses_categories = [
#     "Food",
#     "Transport",
#     "Household",
#     "Pets",
#     "Apparel",
#     "Beauty",
#     "Health",
#     "Education",
#     "Social Life",
#     "Gift",
# ]

def open_update_expenses_window(update_expenses_frame):
    for widget in update_expenses_frame.winfo_children():
        widget.destroy()
      
    categories = db.update_categories_list()  

    #Element will be use (font, image)  
    my_font = CTkFont("font/Poppins-Bold.ttf")
    save_icon = Image.open("icon/saved_icon.png")
    calendar_icon = Image.open("icon/calendar_icon.png")
    expenses_icon = Image.open("icon/expenses_icon.png")
    category_icon = Image.open("icon/category_icon.png")
    note_icon = Image.open("icon/note_icon.png")

    #Label for Update Expenses
    update_expenses_title_label = CTkLabel(update_expenses_frame, text="Update Expenses", 
                                           font=CTkFont("font/Poppins-Bold.ttf",50,"bold") , text_color="#6965A3")
    update_expenses_title_label.place(relx=0.05, rely=0.08, anchor="w")

    #Label for date
    date_picker_label = CTkLabel(update_expenses_frame, text="Date :", font=CTkFont("font/Poppins-Bold.ttf",35))
    date_picker_label.place(relx=0.07, rely=0.18, anchor="w")

    date_icon_label = CTkLabel(update_expenses_frame, text="",image= CTkImage(calendar_icon) )
    date_icon_label.place(relx=0.05, rely=0.18, anchor="w")

    def update_date_format():
        date_entry.set_date(date_entry.get_date().strftime("%d-%m-%Y"))
        
    #DateEntry widget for selecting date
    date_entry = DateEntry(update_expenses_frame, width=14, borderwidth=2, relief="groove", 
                           selectmode="day", date_pattern="dd-mm-yyyy", font=("Helvetica", 12))
    date_entry.place(relx=0.2, rely=0.18, anchor="w")
    date_entry.bind("<<DateEntrySelected>>", update_date_format)

    #Label for expenses amount
    expenses_amount_label = CTkLabel(update_expenses_frame, text="Expenses : ", font=CTkFont("font/Poppins-Bold.ttf",35))
    expenses_amount_label.place(relx=0.07, rely=0.26, anchor="w")

    expenses_icon_label = CTkLabel(update_expenses_frame, text="",image= CTkImage(expenses_icon) )
    expenses_icon_label.place(relx=0.05, rely=0.26, anchor="w")

    def amount_entry_font_change(expenses_amount_entry):
        expenses_amount = expenses_amount_entry.get
        expenses_amount_entry.configure(font=CTkFont("font/Poppins.ttf",35))

    #Entry for expenses amount
    expenses_amount_entry = CTkEntry(update_expenses_frame, width=150, height=34)
    expenses_amount_entry.place(relx=0.2, rely=0.26, anchor="w")
    expenses_amount_entry.bind("<KeyRelease>", amount_entry_font_change)

    #Label for expenses category
    expenses_categories_label = CTkLabel(update_expenses_frame, text="Category :", font=CTkFont("font/Poppins-Bold.ttf",35))
    expenses_categories_label.place(relx=0.07, rely=0.34, anchor="w")

    category_icon_label = CTkLabel(update_expenses_frame, text="",image= CTkImage(category_icon) )
    category_icon_label.place(relx=0.05, rely=0.34, anchor="w")

    category_var = StringVar()
    #dropdown expenses category menu
    expenses_categories_menu = CTkOptionMenu(update_expenses_frame, values=categories, variable=category_var, width=150, height=34, fg_color="#6965A3")
    expenses_categories_menu.place(relx=0.2, rely=0.34, anchor="w")

    #Label for note
    expenses_note_label = CTkLabel(update_expenses_frame, text="Note :", font=CTkFont("font/Poppins-Bold.ttf",35))
    expenses_note_label.place(relx=0.07, rely=0.42, anchor="w")

    note_icon_label = CTkLabel(update_expenses_frame, text="",image= CTkImage(note_icon) )
    note_icon_label.place(relx=0.05, rely=0.42, anchor="w")


    def note_entry_font_change(event):
        text = expenses_note_entry.get
        expenses_note_entry.configure(font=CTkFont("font/Poppins.ttf",35))

    #Entry for note
    expenses_note_entry = CTkEntry(update_expenses_frame, width=150, height=34)
    expenses_note_entry.place(relx=0.2, rely=0.42, anchor="w")
    expenses_note_entry.bind("<KeyRelease>", note_entry_font_change)

    def save_expenses():
        expenses_date = date_entry.get_date()
        expenses_amount = expenses_amount_entry.get()
        expenses_categories = expenses_categories_menu.get()
        expenses_note = expenses_note_entry.get()
        # expenses_data.append((expenses_date, expenses_amount, expenses_categories, expenses_note))
        db.insert_expenses_to_table(expenses_date,expenses_amount,expenses_categories,expenses_note)
        # update_expenses_window.destroy()

    #Button to save expenses
    save_expenses_button = CTkButton(update_expenses_frame, text="Save Expenses", font=CTkFont("font/Poppins-Bold.ttf",30), 
                                     fg_color="#6965A3", hover_color="#8885B6", image=CTkImage(save_icon), command=save_expenses)
    save_expenses_button.place(relx=0.05, rely=0.6, anchor="w")
