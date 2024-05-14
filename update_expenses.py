from customtkinter import *
from tkcalendar import DateEntry
from datetime import datetime
from PIL import Image

expenses_categories = [
    "Food",
    "Transport",
    "Household",
    "Pets",
    "Apparel",
    "Beauty",
    "Health",
    "Education",
    "Social Life",
    "Gift",
]

expenses_data = []

def open_update_expenses_window():
    update_expenses_window = CTkToplevel()
    update_expenses_window.title("Update Expenses")
    update_expenses_window.geometry("900x400")
    update_expenses_window.wm_attributes("-topmost",True)

    expenses_frame = CTkFrame(master=update_expenses_window, width=700, height=600,border_width=5, border_color="#3F3D65", corner_radius=15)
    expenses_frame.grid(row=10, column=0, padx=20, pady=5)

    #Label for Update Expenses
    update_expenses_title_label = CTkLabel(update_expenses_window, text="Update Expenses", font=CTkFont("font/Poppins-Bold.ttf",50,"bold") , text_color="#6965A3")
    update_expenses_title_label.grid(row=1, column=0, padx=20, pady=5, sticky="w")

    #Label for date
    date_picker_label = CTkLabel(update_expenses_window, text="Date :", font=CTkFont("Poppins-Bold.ttf",30))
    date_picker_label.grid(row=3, column=0, padx=50, pady=5, sticky="w", in_=expenses_frame)

    date_icon_label = CTkLabel(update_expenses_window, text="",image= CTkImage(calendar_icon) )
    date_icon_label.grid(row=3, column=0, padx=20, pady=5, sticky="w", in_=expenses_frame)

    def update_date_format(event):
        date_entry.set_date(date_entry.get_date().strftime("%d-%m-%Y"))
        
    #DateEntry widget for selecting date
    date_entry = DateEntry(update_expenses_window, width=14, borderwidth=2, relief="groove", selectmode="day", date_pattern="dd-mm-yyyy", font=("Helvetica", 12))
    date_entry.grid(row=3, column=1, padx=10, pady=5, sticky="w", in_=expenses_frame)
    date_entry.bind("<<DateEntrySelected>>", update_date_format)

    #Label for expenses amount
    expenses_amount_label = CTkLabel(update_expenses_window, text="Expenses : ", font=CTkFont("font/Poppins-Bold.ttf",30))
    expenses_amount_label.grid(row=6, column=0, padx=50, pady=5, sticky="w", in_=expenses_frame)

    expenses_icon_label = CTkLabel(update_expenses_window, text="",image= CTkImage(expenses_icon) )
    expenses_icon_label.grid(row=6, column=0, padx=20, pady=5, sticky="w", in_=expenses_frame) 

    def amount_entry_font_change(event):
        text = expenses_amount_entry.get
        expenses_amount_entry.configure(font=CTkFont("font/Poppins.ttf",26))

    #Entry for expenses amount
    expenses_amount_entry = CTkEntry(update_expenses_window, width=150, height=34)
    expenses_amount_entry.grid(row=6, column=1, padx=10, pady=5, sticky="w", in_=expenses_frame)
    expenses_amount_entry.bind("<KeyRelease>", amount_entry_font_change)

    #Label for expenses category
    expenses_categories_label = CTkLabel(update_expenses_window, text="Category :", font=CTkFont("Poppins-Bold.ttf",30))
    expenses_categories_label.grid(row=9, column=0, padx=50, pady=5, sticky="w", in_=expenses_frame)

    category_icon_label = CTkLabel(update_expenses_window, text="",image= CTkImage(category_icon) )
    category_icon_label.grid(row=9, column=0, padx=20, pady=5, sticky="w", in_=expenses_frame) 

    #dropdown expenses category menu
    expenses_categories_menu = CTkOptionMenu(update_expenses_window, values=expenses_categories, fg_color="#6965A3")
    expenses_categories_menu.grid(row=7, column=1, padx=10, pady=5, sticky="w")

    #Label for note
    expenses_note_label = CTkLabel(update_expenses_window, text="Note :", font=CTkFont("Poppins-Bold.ttf",30))
    expenses_note_label.grid(row=12, column=0, padx=50, pady=5, sticky="w", in_=expenses_frame)

    note_icon_label = CTkLabel(update_expenses_window, text="",image= CTkImage(note_icon) )
    note_icon_label.grid(row=12, column=0, padx=20, pady=5, sticky="w", in_=expenses_frame) 

    def note_entry_font_change(event):
        text = expenses_note_entry.get
        expenses_note_entry.configure(font=CTkFont("font/Poppins.ttf",26))

    #Entry for note
    expenses_note_entry = CTkEntry(update_expenses_window, width=150, height=34)
    expenses_note_entry.grid(row=12, column=1, padx=10, pady=5, sticky="w", in_=expenses_frame)
    expenses_note_entry.bind("<KeyRelease>", note_entry_font_change)

    def save_expenses():
        expenses_date = date_entry.get_date()
        expenses_amount = expenses_amount_entry.get()
        expenses_categories = expenses_categories_menu.get()
        expenses_note = expenses_note_entry.get()
        expenses_data.append((expenses_date, expenses_amount, expenses_categories, expenses_note))
        db.insert_expenses_to_table(expenses_date,expenses_amount,expenses_categories,expenses_note)
        # update_expenses_window.destroy()


    #Button to save expenses
    save_expenses_button = CTkButton(update_expenses_window, text="Save Expenses", font=CTkFont("Poppins-Bold.ttf",25), fg_color="#6965A3", hover_color="#8885B6", image=CTkImage(save_icon), command=save_expenses)
    save_expenses_button.grid(row=18, column=0, padx=10, pady=5, sticky="w", in_=expenses_frame)

    clock_frame = CTkFrame(master=update_expenses_window, width=700, height=600,border_width=5, border_color="#3F3D65", corner_radius=15)
    clock_frame.grid(row=10, column=4, padx=20, pady=5, sticky="n")

    def clock_time ():
        clock_string = strftime("%H:%M:%S %p")
        clock_label.configure(text=clock_string)
        clock_label.after(1000, clock_time)

    clock_label = CTkLabel(update_expenses_window, font=CTkFont("Jersey.ttf", 40, "bold"))
    clock_label.grid(row=0, column=0, padx=60, pady=5, sticky="e", in_=clock_frame)
    clock_time()