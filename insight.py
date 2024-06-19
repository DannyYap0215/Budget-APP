from customtkinter import *
import expenses_piechart
import income_piechart
import usage_barchart
from PIL import Image

expenses_icon = Image.open("icon/expenses_history.png")
income_icon = Image.open("icon/income.png")
usage_icon = Image.open("icon/usage.png")

# Mei Ting part clear frame b4 open new one
def clear_frame(frame):
    for widget in frame.winfo_children():
        widget.destroy()

def open_expenses_piechart(insight_frame_two):
        expenses_piechart.open_expenses_piechart_window(insight_frame_two)

def open_income_piechart(insight_frame_two):
        income_piechart.open_income_piechart_window(insight_frame_two)

def open_usage_barchart(insight_frame_two):
        usage_barchart.open_usage_barchart_window(insight_frame_two)

def open_insight_window(insight_frame):
    clear_frame(insight_frame)

    insight_frame_two = CTkFrame(master=insight_frame, width=1160, height=1080, corner_radius=10, border_width=2, border_color="#535085", fg_color="#202124")
    insight_frame_two.place(relx=0.23, rely=0.5, anchor="w")

    insight_title_label = CTkLabel(insight_frame, text="Insight", font=CTkFont("font/Poppins-Bold.ttf",50,"bold") ,
                                    text_color="#6965A3")
    insight_title_label.place(relx=0.02, rely=0.08, anchor="w")

    expenses_button = CTkButton(insight_frame, text="Expenses", font=CTkFont("font/Poppins-Bold.ttf",30), 
                                fg_color="#6965A3", hover_color="#8885B6", image=CTkImage(expenses_icon), command=lambda:open_expenses_piechart(insight_frame_two))
    expenses_button.place(relx=0.02, rely=0.18, anchor="w")
    
    income_button = CTkButton(insight_frame, text="Income", font=CTkFont("font/Poppins-Bold.ttf",30), 
                                fg_color="#6965A3", hover_color="#8885B6", image=CTkImage(income_icon), command=lambda:open_income_piechart(insight_frame_two))
    income_button.place(relx=0.02, rely=0.28, anchor="w")
    
    usage_button = CTkButton(insight_frame, text="Usage of Budget", font=CTkFont("font/Poppins-Bold.ttf",30), 
                                fg_color="#6965A3", hover_color="#8885B6", image=CTkImage(usage_icon), command=lambda:open_usage_barchart(insight_frame_two))
    usage_button.place(relx=0.02, rely=0.38, anchor="w")
