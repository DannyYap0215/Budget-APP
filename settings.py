from customtkinter import *
import tkinter as tk
from tkinter import messagebox
import database_test as db
import sqlite3
from PIL import Image
from user_guide import UserGuide

back_icon = Image.open("icon/back_arrow.png")
next_icon = Image.open("icon/next_arrow.png")
delete_icon = Image.open("icon/delete_icon.png")

class Settings():
    def __init__ (self,dashboard_right_frame):
        self.dashboard_right_frame = dashboard_right_frame
        for widget in self.dashboard_right_frame.winfo_children():
            widget.destroy()

        # self.settings_window = CTkToplevel()
        # self.settings_window.title("Settings")
        # self.settings_window.geometry("620x320")
        # self.settings_window.wm_attributes("-topmost",True)
        # self.settings_window.resizable(width=False, height=False)
        # self.settings_window.minsize(620, 320)  
        # self.settings_window.maxsize(620, 320)

        settings_label = CTkLabel(self.dashboard_right_frame, text="Settings", font=CTkFont("font/Poppins-Bold.ttf",50,"bold") , text_color="#6965A3")
        settings_label.place(relx=0.02, rely=0.08, anchor="w")
        
        # self.settings_frame_two = CTkFrame(self.dashboard_right_frame, width=1160, height=1080, corner_radius=10, border_width=2, border_color="#535085", fg_color="#202124")
        # self.settings_frame_two.place(relx=0.23, rely=0.5, anchor="w")

        self.settings_frame = CTkFrame(self.dashboard_right_frame,width=1500, height=1080, corner_radius=10,
                                       border_width=2, border_color="#535085", fg_color="#202124")
        self.settings_frame.place(relx=0.23, rely=0.5, anchor="w")
        self.settings_frame.grid_propagate(False)
        # self.settings_frame.grid_propagate(False) #makes frame stays in shape
        
        # self.button_frame = CTkFrame(self.dashboard_right_frame,
        #                         width=500,height= 1080)
        # self.button_frame.grid(row=0,column=0, sticky="nsew")
        # self.button_frame.grid_propagate(False)

        user_guide_button = CTkButton(self.dashboard_right_frame, text="User Guide", font=CTkFont("font/Poppins-Bold.ttf",30), fg_color="#6965A3", hover_color="#8885B6", command=self.user_guide)
        user_guide_button.place(relx=0.02, rely=0.18, anchor="w")

        change_theme_button = CTkButton(self.dashboard_right_frame, text="Edit Change Theme", font=CTkFont("font/Poppins-Bold.ttf",30), fg_color="#6965A3", hover_color="#8885B6", command=self.user_guide)
        change_theme_button.place(relx=0.02, rely=0.28, anchor="w")

        reset_data_button = CTkButton(self.dashboard_right_frame, text="Reset Data", font=CTkFont("font/Poppins-Bold.ttf",30), fg_color="#6965A3", hover_color="#8885B6", command=self.reset_data)
        reset_data_button.place(relx=0.02, rely=0.38, anchor="w")
        
    def clear_frame(self):
        for widget in self.settings_frame.winfo_children():
            widget.destroy() 
    
    #frame for user_guide
    def user_guide(self) :
        #frame for user guide
        # self.user_guide_frame = CTkFrame(self.settings_frame, width=self.settings_frame.winfo_width(), height=200,corner_radius=0)
        # self.user_guide_frame.grid(row=0,column=0, sticky="nsew")
        # self.user_guide_frame.grid_propagate(False)
        
        #frame for user guide buttons
        self.page = 1
        self.update_user_guide()
        # self.user_guide_button_frame = CTkFrame(self.settings_frame, width=self.settings_frame.winfo_width(), height=60,corner_radius=0)
        # self.user_guide_button_frame.grid(row=1,column=0, sticky="nsew")
        # self.user_guide_button_frame.grid_propagate(False)
        
        
        # back_button = CTkButton(self.settings_frame, text="BACK", font=CTkFont("font/Poppins-Bold.ttf",30), fg_color="#6965A3", bg_color="#1f2124", hover_color="#8885B6",image= CTkImage(back_icon),command=self.previous_page)
        # back_button.place(relx=0.05, rely=0.9, anchor="w")
        # next_button = CTkButton(self.settings_frame, text="NEXT", font=CTkFont("font/Poppins-Bold.ttf",30), fg_color="#6965A3", bg_color="#1f2124", hover_color="#8885B6",image= CTkImage(next_icon),command=self.next_page)
        # next_button.place(relx=0.62, rely=0.9, anchor="w")
    
    
    #functions for user guides
    def update_user_guide(self) :
        self.clear_frame()
        
        if True:
            back_button = CTkButton(self.settings_frame, text="BACK", font=CTkFont("font/Poppins-Bold.ttf",30), fg_color="#6965A3", bg_color="#1f2124", hover_color="#8885B6",image= CTkImage(back_icon),command=self.previous_page)
            back_button.place(relx=0.05, rely=0.9, anchor="w")
            next_button = CTkButton(self.settings_frame, text="NEXT", font=CTkFont("font/Poppins-Bold.ttf",30), fg_color="#6965A3", bg_color="#1f2124", hover_color="#8885B6",image= CTkImage(next_icon),command=self.next_page)
            next_button.place(relx=0.62, rely=0.9, anchor="w")

            if self.page == 1:
                UserGuide.userGuide1(self)
            elif self.page == 2:
                UserGuide.userGuide2(self)
            elif self.page == 3:
                UserGuide.userGuide3(self)
            elif self.page == 4:
                UserGuide.userGuide4(self)
            elif self.page == 5:
                UserGuide.userGuide5(self)
            elif self.page == 6:
                UserGuide.userGuide6(self)
            elif self.page == 7:
                UserGuide.userGuide7(self)
            elif self.page == 8:
                UserGuide.userGuide8(self)
            elif self.page == 9:
                UserGuide.userGuide9(self)
            elif self.page == 10:
                UserGuide.userGuide10(self)
    
            
    def previous_page(self):
        if self.page > 0  and self.page != 0:
            self.page -= 1
            self.update_user_guide()
            print(self.page)
        elif self.page == 0 :
            self.page = 10
            self.update_user_guide()
            print(self.page)

    def next_page(self):
        if self.page > 0 and self.page < 10:
            self.page += 1
            self.update_user_guide()
            print(self.page) 
        elif self.page == 10:
            self.page = 1
            self.update_user_guide()
            print(self.page)    
    
    #data
    def reset_data(self) : #dont delete lol(working)
        self.clear_frame()
        confirm_label = CTkLabel(self.settings_frame, text="Type 'CONFIRM' to reset data:", font=CTkFont("font/Poppins-Bold.ttf",35), justify=LEFT)
        confirm_label.place(relx=0.05, rely=0.18, anchor="w")

        #Mei Ting's Part : Entry font change
        def confirm_entry_font_change(event):
            text = self.confirm_entry.get()
            self.confirm_entry.configure(font=CTkFont("font/Poppins.ttf",35))

        self.confirm_entry = CTkEntry(self.settings_frame, width=200, height=46)
        self.confirm_entry.place(relx=0.05, rely=0.28, anchor="w")
        self.confirm_entry.bind("<KeyRelease>", confirm_entry_font_change)

        confirm_button = CTkButton(self.settings_frame, text="Delete ALL the data", font=CTkFont("font/Poppins-Bold.ttf",30), fg_color="#6965A3", bg_color="#1f2124", hover_color="#8885B6",image= CTkImage(delete_icon), command=self.perform_reset)
        confirm_button.place(relx=0.05, rely=0.38, anchor="w")
    
    def perform_reset(self) :
        if self.confirm_entry.get() == "CONFIRM":
            con = sqlite3.connect('database.db')
            c = con.cursor()
            c.execute("DELETE FROM allocated_income_for_month_2024")
            c.execute("DELETE FROM budget_2024")
            c.execute("DELETE FROM daily_expenses")
            con.commit()
            self.settings_frame.wm_attributes("-topmost", False)
            messagebox.showinfo("Data Reset", "Data has been successfully reset.")
            # self.settings_window.wm_attributes("-topmost", True)
        else:
            self.settings_frame.wm_attributes("-topmost", False)
            messagebox.showerror("Error", "You must type 'CONFIRM' to reset data.")
            self.confirm_entry.delete(0, 'end')
            # self.settings_frame.wm_attributes("-topmost", True)
    
   