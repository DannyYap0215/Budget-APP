import tkinter as tk


months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]



def open_set_income_window():

    def save_budget():
        set_income_window.destroy()

    set_income_window = tk.Toplevel()
    set_income_window.title("Set Income")
    set_income_window.geometry("400x300")

    income_label = tk.Label(set_income_window, text="Income:")
    income_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")
    income_entry = tk.Entry(set_income_window)
    income_entry.grid(row=0, column=1, padx=10, pady=5)
  
    month_issued_label = tk.Label(set_income_window, text="Month Issued:")
    month_issued_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")
    selected_months_var = tk.StringVar(set_income_window)
    selected_months_var.set(months[0])
    month_issued_menu = tk.OptionMenu(set_income_window, selected_months_var, *months)
    month_issued_menu.grid(row=1, column=1, padx=10, pady=5)
  
    save_button = tk.Button(set_income_window, text="Save", command=save_budget)
    save_button.grid(row=4, column=1)

   


