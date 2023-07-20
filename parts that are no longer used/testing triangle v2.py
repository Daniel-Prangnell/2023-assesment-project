from tkinter import *

root= Tk()
can = Canvas(root, width=200, height=200)
can.pack()
shape1={'bounds': [20,80, 80,20, 80,80], 'kind': 'rect', 'fill': True}
shape2={'bounds': [24,78, 79,24, 79,79], 'kind': 'tri', 'fill': True}
can.create_polygon(list(shape1.values())[0],fill='black')
can.create_polygon(list(shape2.values())[0],fill='white')
root.mainloop()