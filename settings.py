from customtkinter import *
import tkinter as tk
from tkinter import messagebox
import database_test as db
import sqlite3
from PIL import Image

class Settings():
    def __init__ (self):
        self.settings_window = CTkToplevel()
        self.settings_window.title("Settings")
        self.settings_window.geometry("620x320")
        self.settings_window.wm_attributes("-topmost",True)
        self.settings_window.resizable(width=False, height=False)
        # self.settings_window.minsize(620, 320)  
        # self.settings_window.maxsize(620, 320)
        
        self.settings_frame = CTkFrame(self.settings_window,
                                width=400,height= 300,
                                fg_color="#1f2124",border_color="#535085",
                                border_width=4,corner_radius=8)
        self.settings_frame.grid(row=0,column=1, sticky="nsew")
        self.settings_frame.grid_propagate(False) #makes frame stays in shape
        
        self.button_frame = CTkFrame(self.settings_window,
                                width=150,height= 300,
                                fg_color="#1f2124",border_color="#535085",
                                border_width=4,corner_radius=8)
        self.button_frame.grid(row=0,column=0, sticky="nsew")
        self.button_frame.grid_propagate(False)

        user_guide_button = CTkButton(self.button_frame, text="User Guide", width = 130, height = 85, command=self.user_guide)
        user_guide_button.grid(row=0, column=0, padx=10, pady=(13,5),  sticky="nsew")

        change_theme_button = CTkButton(self.button_frame, text="Edit Change Theme", width = 130, height = 85, command=self.user_guide)
        change_theme_button.grid(row=1, column=0, padx=10, pady=5, sticky="nsew")

        reset_data_button = CTkButton(self.button_frame, text="Reset Data",width = 130, height = 85, command=self.reset_data)
        reset_data_button.grid(row=2, column=0, padx=10, pady=5, sticky="nsew")
    
    def user_guide(self) :
        self.guide1 = CTkLabel(self.settings_frame, text="First of, you can set up ur monthly income first!", justify = LEFT,font=CTkFont("font/Poppins-Bold.ttf",30,"bold") , text_color="#6965A3", wraplength=380)
        self.guide1.grid(row=0, column=0, padx=10, pady=5, sticky="nsew")
        pass
    
    def reset_data(self) : #dont delete lol(working)
        confirm_label = CTkLabel(self.settings_frame, text="Type 'CONFIRM' to reset data:", justify=LEFT)
        confirm_label.grid(row=0, column=0, padx=10, pady=5, sticky="nsew")

        self.confirm_entry = CTkEntry(self.settings_frame, width=200)
        self.confirm_entry.grid(row=1, column=0, padx=10, pady=5, sticky="nsew")

        confirm_button = CTkButton(self.settings_frame, text="Delete", command=self.perform_reset)
        confirm_button.grid(row=2, column=0, padx=10, pady=5, sticky="nsew")
    
    def perform_reset(self) :
        if self.confirm_entry.get() == "CONFIRM":
            con = sqlite3.connect('database.db')
            c = con.cursor()
            c.execute("DELETE FROM allocated_income_for_month_2024")
            c.execute("DELETE FROM budget_2024")
            c.execute("DELETE FROM daily_expenses")
            con.commit()
            messagebox.showinfo("Data Reset", "Data has been successfully reset.")
        else:
            messagebox.showerror("Error", "You must type 'CONFIRM' to reset data.")
            self.confirm_entry.delete(0, 'end')
    
   