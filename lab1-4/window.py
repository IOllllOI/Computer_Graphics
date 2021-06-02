from tkinter import *
import logic
import algorithms

window = Tk()
window.title('Лабораторные по графике')
window.geometry('+400+400')
# window.minsize(height = 400, width = 600)

function_menu = Menu(window)
window.config(menu = function_menu)

select_functiion = Menu(function_menu, tearoff = 0)

height = 400
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

algorithms.dpf = lambda x, y: canvas.create_oval(x, y, x, y, width = logic.widthInPix)

logic.c_clear = lambda : canvas.delete("all")

def coordinats(x, y):
    str = "Coordinates: X-{} : Y-{}".format(x, y)
    l_coordinates['text'] = str

logic.set_coordinats = lambda x, y:  coordinats(x, y)

# def click(event):
#     if radioKey == False:
#         point1.x = event.x
#         point1.y = event.y
#         radioKey = True
#     else:
#         point2.x = event.x
#         point2.y = event.y
#         canvas.create_line(self, point1.x, point1.y, point2.x, point2.y)
#         radioKey = False



# def create_point(x = 0, y = 0):
#     canvas.create_oval(x, y, x, y, width = widthInPix)


select_functiion.add_command(label = 'Draw', command = logic.select_draw)
select_functiion.add_command(label = 'Demonstration', command = logic.select_demonstration)

function_menu.add_cascade(label = 'Menu', menu = select_functiion)



b_pencil = Button(lf_tools_panel, text = '🖊', command = logic.c_pencil)
b_pencil.pack(side = LEFT)

b_line = Button(lf_tools_panel, text = '⁄', command = logic.c_line)
b_line.pack(side = LEFT)

b_circle = Button(lf_tools_panel, text = '○', command = logic.c_circle)
b_circle.pack(side = LEFT)

b_ellipse = Button(lf_tools_panel, text = '⬭', command = logic.c_ellipse)
b_ellipse.pack(side = LEFT)

b_clear = Button(lf_tools_panel, text = '↺', command = logic.c_clear)
b_clear.pack(side = LEFT)

b_back = Button(lf_tools_panel, text = '⇦', command = logic.come_back)
b_back.pack(side = LEFT)

canvas.bind('<Motion>', logic.move)
canvas.bind('<B1-Motion>', logic.drag)
canvas.bind('<Button-1>', logic.click)
canvas.bind('<B1-Shift>')


window.mainloop()