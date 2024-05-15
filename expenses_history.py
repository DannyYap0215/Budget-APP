from customtkinter import *
from tkcalendar import DateEntry
from tkinter import ttk
from update_expenses import expenses_data
from PIL import Image

month = [
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

calendar_icon = Image.open("icon/calendar_icon.png")

def open_expenses_history_window(expenses_data):
    expenses_history_window = CTkToplevel()
    expenses_history_window.title("Expenses History")
    expenses_history_window.geometry("800x600")
    expenses_history_window.wm_attributes("-topmost",True)
    
    #Label for Update Expenses
    expenses_history_title_label = CTkLabel(expenses_history_window, text="Expenses History", font=CTkFont("font/Poppins-ExtraBold",50, "bold"), text_color="#6965A3")
    expenses_history_title_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")

    #Month Label
    month_label = CTkLabel(expenses_history_window, text="Select Month:", font=CTkFont("font/Poppins-ExtraBold",30))
    month_label.grid(row=3, column=0, padx=50, pady=5, sticky="w")

    date_icon_label = CTkLabel(expenses_history_window, text="",image= CTkImage(calendar_icon) )
    date_icon_label.grid(row=3, column=0, padx=20, pady=5, sticky="w")

    month_set = set (expense[0].strftime("%B") for expense in expenses_data) #Extract month from the date entered
    month_list = sorted (month_set) #Sort the extracted month

    #Dropdown menu for month
    month_var = StringVar()
    month_dropdown = CTkOptionMenu(expenses_history_window, values=month_list, variable=month_var, fg_color="#6965A3") 
    month_dropdown.grid(row=3, column=1, padx=10, pady=5, sticky=N)

    def update_expenses_treeview():
        selected_month = month_var.get()
        filtered_expenses = [expense for expense in expenses_data if expense[0].strftime("%B") == selected_month]
        for item in expenses_treeview.get_children(): #Clear existing items in the treeview
            expenses_treeview.delete(item) 
        for expense in filtered_expenses: #Insert filtered expenses into the treeview
            formatted_date = expense[0].strftime("%d-%m-%Y")
            expenses_treeview.insert("", "end", values=(formatted_date,) + expense[1:])

    #Button to update expenses treeview
    update_icon = Image.open("icon/update_icon.png")
    update_button = CTkButton(expenses_history_window, text="Update", font=CTkFont("font/Poppins-ExtraBold",15), fg_color="#6965A3", hover_color="#8885B6", image=CTkImage(update_icon), command=update_expenses_treeview)
    update_button.grid(row=3, column=2, padx=10, pady=5, sticky="w")
    

    expenses_treeview = ttk.Treeview(expenses_history_window, columns=("Date", "Amount", "Category", "Note"), show="headings")
    expenses_treeview.heading("Date", text="Date")
    expenses_treeview.heading("Amount", text="Amount (RM)")
    expenses_treeview.heading("Category", text="Category")
    expenses_treeview.heading("Note", text="Note")
    expenses_treeview.grid(row=5, column=0, columnspan=3, padx=10, pady=5)

    #Insert all expenses data initially
    for expense in expenses_data:
        formatted_date = expense[0].strftime("%d-%m-%Y")
        expenses_treeview.insert("", "end", values=(formatted_date,) + expense[1:])

    #Update the treeview based on the initially selected month
    update_expenses_treeview()