import tkinter as tk
from tkcalendar import DateEntry

def open_update_expenses_window():
    update_expenses_window = tk.Toplevel()
    update_expenses_window.title("Update Expenses")
    update_expenses_window.geometry("400x300")
    
    #added a date picker
    def date_update():
        date_picker = DateEntry (update_expenses_window, selectmode="day")
        date_picker.grid(row=1, column=1, padx=15)
        date = date_picker.get_date()
        date_string = date.strftime ("%d-%m-%y") #for the date format in d-m-y form
        date_picker_label.config (text=date_string)
        date_picker_label = tk.Label (update_expenses_window)
        date_picker_label.grid (row=1, column=3)
        date_picker_button = tk.Button (update_expenses_window, text="Get Date", command=lambda:date_update())
        date_picker_button.grid (row=1, column=2 )
