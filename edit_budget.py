import tkinter as tk

def open_edit_budget_window():
    def save_budget():
        income_value = income_entry.get()
        month_issued_value = month_issued_entry.get()
        print(income_value)
        print(month_issued_value)
        edit_budget_window.destroy()

    edit_budget_window = tk.Toplevel()
    edit_budget_window.title("Edit Budget")

    income_label = tk.Label(edit_budget_window, text="Income:")
    income_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")
    income_entry = tk.Entry(edit_budget_window)
    income_entry.grid(row=0, column=1, padx=10, pady=5)

    month_issued_label = tk.Label(edit_budget_window, text="Month Issued:")
    month_issued_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")
    month_issued_entry = tk.Entry(edit_budget_window)
    month_issued_entry.grid(row=1, column=1, padx=10, pady=5)

    save_button = tk.Button(edit_budget_window, text="Save", command=save_budget)
    save_button.grid(row=2, columnspan=2, pady=10)
