from customtkinter import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib import pyplot as plt
 
expenses_categories = ["Food",
    "Transport",
    "Household",
    "Pets",
    "Apparel",
    "Beauty",
    "Health",
    "Education",
    "Social Life",
    "Gift",]
wieght = [800,500,200,1000,200,500,100,1000,500,500]
colours = ["#ffcd8e", "#ffb255", "#ff8ca1", "#f45f74", "#ffc9ed", "#b77ea3", "#8fd7d7", "#00b0be", "#bdd373", "#98c127", ]

def open_insight_window():
    insight_window = CTk()
    insight_window.title("Expenses Pie Chart")
    insight_window.geometry("520x520+300+200")

    fig = plt.figure()
    ax = fig.add_axes([0,0,1,1])
    ax.pie(wieght, labels = expenses_categories , autopct='%1.2f%%',colors=colours)

    canvasbar = FigureCanvasTkAgg(fig, master=insight_window)
    canvasbar.draw()
    canvasbar.get_tk_widget().place(relx=0.5, rely=0.5, anchor=CENTER)  
    # show the barchart on the ouput window

    insight_window.mainloop() 