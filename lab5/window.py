from tkinter import *
import logic
import algorithms

window = Tk()
window.title('лабораторные по графике № 5')
window.geometry('+400+200')
# window.minsize(height = 400, width = 600)

function_menu = Menu(window)
window.config(menu = function_menu)

select_functiion = Menu(function_menu, tearoff = 0)

height = 600
width = 600

lf_tools_panel = LabelFrame(window, text = 'Tools panel',width = width, height = 50)
lf_tools_panel.pack(side = TOP, fill = X)
f_coordinates = Frame(window, width = width, height = 20)
f_coordinates.pack(side = TOP, fill = X)

canvas = Canvas(window, height = height, width = width, bg = 'yellow')
canvas.pack(side = TOP, expand = True, fill = BOTH)

# canvas2 = Canvas(canvas, height = height, width = width)
# canvas2.pack(side = TOP, expand = True, fill = BOTH)

l_coordinates = Label(f_coordinates, text = 'Coordinates:', height = 1)
l_coordinates.pack(side = LEFT)



# coordinates = Label(f_coordinates, height = 40, textvariable = str_coordinates).pack(side = LEFT)

# class Point:
#     x = 0
#     y = 0
#
# point1 = Point()
# point2 = Point()

algorithms.dpf = lambda x, y: canvas.create_oval(x, y, x + 1, y + 1, width = logic.widthInPix)
logic.c_clear = lambda : canvas.delete("all")

def clear_shapes():

    canvas.delete("all")
    logic.delete_shapes()
    canvas.create_oval(algorithms.cx, algorithms.cy, algorithms.cx + 5, algorithms.cy + 5)

def coordinats(x, y):
    str = "Coordinates: X-{} : Y-{}".format(x, y)
    l_coordinates['text'] = str

logic.set_coordinats = lambda x, y:  coordinats(x, y)

b_clear = Button(lf_tools_panel, text = '↺', command = clear_shapes)
b_clear.pack(side = LEFT)

b_rotation = Button(lf_tools_panel, text = '⁐', command = logic.rotarion_radio_b)
b_rotation.pack(side = LEFT)

b_ret = Button(lf_tools_panel, text = 'return', command = logic.returnS)
b_ret.pack(side = LEFT)

canvas.bind('<Motion>', logic.move)
canvas.bind('<B1-Motion>', logic.drag)
canvas.bind('<Button-1>', logic.click)

canvas.create_oval(algorithms.cx, algorithms.cy, algorithms.cx + 5, algorithms.cy + 5)

window.mainloop()