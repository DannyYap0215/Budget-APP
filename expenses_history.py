from customtkinter import *
from tkcalendar import DateEntry
from tkinter import ttk
from PIL import Image
import database_test as db
import sqlite3

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
search_icon = Image.open("icon/search_icon.png")

def clear_frame(frame):
    for widget in frame.winfo_children():
        widget.destroy()

def open_expenses_history_window(expenses_history_frame):
    clear_frame(expenses_history_frame)

    #Label for Update Expenses
    expenses_history_title_label = CTkLabel(expenses_history_frame, text="Expenses History", 
                                            font=CTkFont("font/Poppins-ExtraBold",50, "bold"), text_color="#6965A3")
    expenses_history_title_label.place(relx=0.05, rely=0.08, anchor="w")

    #Month Label
    month_label = CTkLabel(expenses_history_frame, text="Select Month:", font=CTkFont("font/Poppins-ExtraBold",35))
    month_label.place(relx=0.07, rely=0.18, anchor="w")

    date_icon_label = CTkLabel(expenses_history_frame, text="",image= CTkImage(calendar_icon) )
    date_icon_label.place(relx=0.05, rely=0.18, anchor="w")

    # month_set = set (expense[0].strftime("%B") for expense in expenses_data) #Extract month from the date entered
    # month_list = sorted (month_set) #Sort the extracted month

    custom_font = CTkFont("font/Poppins-Bold.ttf", size=30)

    #Dropdown menu for month
    month_var = StringVar()
    
    month_dropdown = CTkOptionMenu(expenses_history_frame, values=month, variable=month_var, font=custom_font, fg_color="#6965A3", button_color="#3F3D65", button_hover_color="#A7A5C9") 
    month_dropdown.place(relx=0.26, rely=0.18, anchor="w")

    def update_expenses_treeview():
        selected_month = month_var.get()
        print(selected_month)
        con = sqlite3.connect("database.db")
        c = con.cursor()
        
        #set de. to be daily_expenses and cd. as category_data and on the codintion the cat_ID of de = cat_ID of cd #new stuff :D-danny
        c.execute("SELECT de.date, de.expenses, cd.category, de.note FROM daily_expenses de JOIN category_data cd ON de.cat_ID = cd.cat_ID WHERE de.months = ?", (selected_month,))
        rows = c.fetchall()
        
        # Clear existing items in the treeview
        for item in expenses_treeview.get_children():
            expenses_treeview.delete(item)
        
        # Insert fetched expenses into the treeview
        for expense in rows:
            expenses_treeview.insert("", "end", values=(expense[0], expense[1], expense[2], expense[3]))  
            
    def search_function():
        search_query = search_var.get()
        
        con = sqlite3.connect("database.db")
        c = con.cursor()    
        c.execute("SELECT de.date, de.expenses ,cd.category, de.note FROM daily_expenses de JOIN category_data cd ON de.cat_ID = cd.cat_ID WHERE de.months LIKE ? OR cd.category LIKE ? OR de.expenses LIKE ? OR de.date LIKE ? OR de.note LIKE ?", 
            (f"%{search_query}%" , f"%{search_query}%" , f"%{search_query}%" , f"%{search_query}%" , f"%{search_query}%"))
        rows = c.fetchall()
        print(rows)
        print(search_query)
        for item in expenses_treeview.get_children():
                expenses_treeview.delete(item)
            
        for expense in rows:
            expenses_treeview.insert("", "end", values=(expense[0], expense[1], expense[2], expense[3])) 
    
            
    # def update_expenses_treeview():
    #     selected_month = month_var.get()
        
    #     filtered_expenses = [expense for expense in expenses_data if expense[0].strftime("%B") == selected_month]
    #     for item in expenses_treeview.get_children(): #Clear existing items in the treeview
    #         expenses_treeview.delete(item) 
    #     for expense in filtered_expenses: #Insert filtered expenses into the treeview
    #         formatted_date = expense[0].strftime("%d-%m-%Y")
    #         expenses_treeview.insert("", "end", values=(formatted_date,) + expense[1:])


    #Button to update expenses treeview
    update_icon = Image.open("icon/update_icon.png")
    update_button = CTkButton(expenses_history_frame, text="Update Month", font=CTkFont("font/Poppins-ExtraBold",30), fg_color="#6965A3", hover_color="#8885B6", image=CTkImage(update_icon), command=update_expenses_treeview)
    update_button.place(relx=0.43, rely=0.18, anchor="w")

    #Search Label
    search_label = CTkLabel(expenses_history_frame, text="Search Your Expenses:", font=CTkFont("font/Poppins-ExtraBold",35))
    search_label.place(relx=0.07, rely=0.26, anchor="w")

    search_icon_label = CTkLabel(expenses_history_frame, text="",image= CTkImage(search_icon) )
    search_icon_label.place(relx=0.05, rely=0.26, anchor="w")

    def search_entry_font_change(event):
        text = search_entry.get
        search_entry.configure(font=CTkFont("font/Poppins.ttf",30))

    #Danny 's search functions
    search_var = StringVar()
    search_entry = CTkEntry(expenses_history_frame,textvariable=search_var, width=300, height=46)
    search_entry.place(relx=0.36, rely=0.26, anchor="w")
    search_entry.bind("<KeyRelease>", search_entry_font_change)

    find_icon = Image.open("icon/find_icon.png") #Mei Ting's GUI
    search_button = CTkButton(expenses_history_frame, text="Search", font = CTkFont("font/Poppins-ExtraBold",30), fg_color="#6965A3", hover_color="#8885B6", image=CTkImage(find_icon), command=search_function)
    search_button.place(relx=0.61, rely=0.26, anchor="w")

    expenses_treeview_style = ttk.Style()
    expenses_treeview_style.configure("Treeview.Heading", font=("Poppins-ExtraBold", 20))
    expenses_treeview_style.configure("Treeview", font=("Poppins", 15))
    expenses_treeview_style.configure("Treeview", rowheight=30)

    expenses_treeview = ttk.Treeview(expenses_history_frame, columns=("Date", "Amount", "Category", "Note"), show="headings", height=21, style="Treeview")
    expenses_treeview.heading("Date", text="Date")
    expenses_treeview.heading("Amount", text="Amount (RM)")
    expenses_treeview.heading("Category", text="Category")
    expenses_treeview.heading("Note", text="Note")

    expenses_treeview.column("Date", width=200)
    expenses_treeview.column("Amount", width=250)
    expenses_treeview.column("Category", width=200)
    expenses_treeview.column("Note", width=300)

    expenses_treeview.place(relx=0.05, rely=0.63, anchor="w")


    #Insert all expenses data initially
    # for expense in expenses_data:
    #     formatted_date = expense[0].strftime("%d-%m-%Y")
    #     expenses_treeview.insert("", "end", values=(formatted_date,) + expense[1:])

    #Update the treeview based on the initially selected month


    update_expenses_treeview()
   