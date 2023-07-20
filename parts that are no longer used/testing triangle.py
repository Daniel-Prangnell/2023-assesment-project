from tkinter import *



root= Tk()
can = Canvas(root, width=200, height=200)
can.pack()
points_outer = [20,80, 80,20, 80,80]
can.create_polygon(points_outer, fill='white')
root.mainloop()