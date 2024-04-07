import tkinter as tk

#main window
root = tk.Tk()
root.title("Tkinter Sample")
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.geometry(f"{screen_width}x{screen_height}")

def toggle_fullscreen(event=None):
    state = not root.attributes('-fullscreen') #True or False basically 
    root.attributes('-fullscreen', state)

label = tk.Label(root, text="Hello, Tkinter!")
label.pack(pady=10)

button = tk.Button(root, text="Click Me!", command=toggle_fullscreen)
button.pack()


root.bind("<F11>", toggle_fullscreen)

root.mainloop()
