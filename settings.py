from customtkinter import *
import tkinter as tk
from tkinter import messagebox
import database_test as db
import sqlite3
from PIL import Image
from user_guide import UserGuide

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
                                width=400,height= 300)
        self.settings_frame.grid(row=0,column=1, sticky="nsew")
        self.settings_frame.grid_propagate(False) #makes frame stays in shape
        
        self.button_frame = CTkFrame(self.settings_window,
                                width=150,height= 300)
        self.button_frame.grid(row=0,column=0, sticky="nsew")
        self.button_frame.grid_propagate(False)

        user_guide_button = CTkButton(self.button_frame, text="User Guide", width = 130, height = 85, command=self.user_guide)
        user_guide_button.grid(row=0, column=0, padx=10, pady=(13,5),  sticky="nsew")

        change_theme_button = CTkButton(self.button_frame, text="Edit Change Theme", width = 130, height = 85, command=self.user_guide)
        change_theme_button.grid(row=1, column=0, padx=10, pady=5, sticky="nsew")

        reset_data_button = CTkButton(self.button_frame, text="Reset Data",width = 130, height = 85, command=self.reset_data)
        reset_data_button.grid(row=2, column=0, padx=10, pady=5, sticky="nsew")
        
    def clear_frame(self):
        for widget in self.settings_frame.winfo_children():
            widget.destroy() 
    
    #frame for user_guide
    def user_guide(self) :
        #frame for user guide
        self.user_guide_frame = CTkFrame(self.settings_frame, width=self.settings_frame.winfo_width(), height=self.settings_frame.winfo_height()-60,corner_radius=0)
        self.user_guide_frame.grid(row=0,column=0, sticky="nsew")
        self.user_guide_frame.grid_propagate(False)
        
        #frame for user guide buttons
        self.page = 1
        self.update_user_guide()
        self.user_guide_button_frame = CTkFrame(self.settings_frame, width=self.settings_frame.winfo_width(), height=60,corner_radius=0)
        self.user_guide_button_frame.grid(row=1,column=0, sticky="nsew")
        self.user_guide_button_frame.grid_propagate(False)
        
        
        back_button = CTkButton(self.user_guide_button_frame, text="BACK",command=self.previous_page)
        back_button.grid(row=0,column=0, padx=(53,0), pady=(13,5),sticky = "e")
        next_button = CTkButton(self.user_guide_button_frame, text="NEXT",command=self.next_page)
        next_button.grid(row=0,column=1, padx=10, pady=(13,5),sticky = "w")
        
        
    
    #functions for user guides
    def update_user_guide(self) :
        for widget in self.user_guide_frame.winfo_children():
            widget.destroy()
        
        if self.page == 1:
            UserGuide.userGuide1(self)
        elif self.page == 2:
            UserGuide.userGuide2(self)
        elif self.page == 3:
            UserGuide.userGuide3(self)
            
    def previous_page(self):
        if self.page > 0 and self.page != 1:
            self.page -= 1
            self.update_user_guide()
            print(self.page)
        else :
            pass

    def next_page(self):
        if self.page > 0 and self.page < 3:
            self.page += 1
            self.update_user_guide()
            print(self.page) 
        elif self.page == 3:
            self.page = 1
            self.update_user_guide()
            print(self.page)    
    
    #data
    def reset_data(self) : #dont delete lol(working)
        self.clear_frame()
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
            self.settings_window.wm_attributes("-topmost", False)
            messagebox.showinfo("Data Reset", "Data has been successfully reset.")
            self.settings_window.wm_attributes("-topmost", True)
        else:
            self.settings_window.wm_attributes("-topmost", False)
            messagebox.showerror("Error", "You must type 'CONFIRM' to reset data.")
            self.confirm_entry.delete(0, 'end')
            self.settings_window.wm_attributes("-topmost", True)
    
   