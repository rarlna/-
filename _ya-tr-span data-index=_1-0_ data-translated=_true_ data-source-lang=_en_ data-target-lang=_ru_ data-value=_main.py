from tkinter import *
import random
def button_1():
    canvas.configure(random.choice(shapes))
    
    
root=Tk()
root.title("случайные фигуры")
root.geometry(500x200)

shapes=[canvas1, canvas2, canvas3]

canvas=Canvas(root, width=200, height=200, bg='white')
canvas.pack()

canvas1=Canvas(root, width=200, height=200, bg='white')
canvas1.pack()
canvas1.create_rectangle(15, 15, 190, 110)

canvas2=Canvas(root, width=200, height=200, bg='white')
canvas2.pack()
canvas2.create_circle(15, 15, 190, 110)

canvas3=Canvas(root, width=200, height=200, bg='white')
canvas3.pack()
canvas3.create_square(15, 15, 190, 110)

Button(text='случайная фигура', command=button_1).pack()

root.mainloop()