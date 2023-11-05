import tkinter as tk

x = 0
def change_text():
    global x
    var.set(x)
    x +=1
    root.after(100,change_text)#instead of a while loop that block the mainloop

root = tk.Tk()
var = tk.StringVar()
lab = tk.Label(root, textvariable=var)
lab.pack()
change_text()

root.mainloop()