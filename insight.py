from customtkinter import *

def createPieChart(canvas,PieV,colV):
    total = sum(PieV)
    st = 0
    coord = 100, 100, 300, 300
    for val,col in zip(PieV,colV):   
        extent = val / total * 360 
        canvas.create_arc(coord,start=st,extent = extent,fill=col,outline=col)
        st += extent

def open_insight_window():
    insight_window = CTk()
    insight_window.title("Pie Chart")
    insight_window.geometry("520x520+300+200")
    
    canvas = CTkCanvas(insight_window,width=500,height=500)
    canvas.place(x=50,y=50)

    PieV=[25,45,10,20]
    colV=["Red","Yellow","Green","Blue"]
    createPieChart(canvas,PieV,colV)   

    insight_window.mainloop()
