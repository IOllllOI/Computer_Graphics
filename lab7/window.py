from tkinter import *
import logic
import algorithms
import palette

window = Tk()
window.title('Лабораторные по графике')
window.geometry('+400+400')
# window.minsize(height = 400, width = 600)

function_menu = Menu(window)
window.config(menu = function_menu)

select_functiion = Menu(function_menu, tearoff = 0)

height = 600
width = 600

lf_tools_panel = LabelFrame(window, text = 'Tools panel',width = width)
lf_tools_panel.pack(side = TOP, fill = X)
f_coordinates = Frame(window, width = width)
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

algorithms.dpf = lambda x, y: canvas.create_oval(x, y, x, y, width = logic.widthInPix,
                                                 fill=palette.curr_color, outline=palette.curr_color)

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

# Разметка палитры

palette_panel = LabelFrame(lf_tools_panel, text = 'Палитра')
palette_panel.pack(side = LEFT, fill = X)

b_colorchoser = Button(palette_panel, width='3', height='3',command=palette.changeColor)
b_colorchoser.pack(side = LEFT)

f_RGB = Frame(palette_panel)
f_RGB.pack(side = LEFT)
fl_RGB = Frame(f_RGB)
fl_RGB.pack(side = LEFT)
fe_RGB = Frame(f_RGB)
fe_RGB.pack(side = LEFT)

lR = Label(fl_RGB, text = "R")
lR.pack(side = TOP)
eR = Entry(fe_RGB, width=8)
eR.pack(side = TOP)

lG = Label(fl_RGB, text = "G")
lG.pack(side = TOP)
eG = Entry(fe_RGB, width=8)
eG.pack(side = TOP)

lB = Label(fl_RGB, text = "B")
lB.pack(side = TOP)
eB = Entry(fe_RGB, width=8)
eB.pack(side = TOP)

f_HSV = Frame(palette_panel)
f_HSV.pack(side = LEFT)
fl_HSV = Frame(f_HSV)
fl_HSV.pack(side = LEFT)
fe_HSV = Frame(f_HSV)
fe_HSV.pack(side = LEFT)

lH = Label(fl_HSV, text = "H", justify=LEFT)
lH.pack(side = TOP)
eH = Entry(fe_HSV, width=8)
eH.pack(side = TOP)

lS = Label(fl_HSV, text = "S", justify=LEFT)
lS.pack(side = TOP)
eS = Entry(fe_HSV, width=8)
eS.pack(side = TOP)

lV = Label(fl_HSV, text = "V", justify=LEFT)
lV.pack(side = TOP)
eV = Entry(fe_HSV, width=8)
eV.pack(side = TOP)

f_CMYK = Frame(palette_panel)
f_CMYK.pack(side = LEFT)
fl_CMYK = Frame(f_HSV)
fl_CMYK.pack(side = LEFT)
fe_CMYK = Frame(f_HSV)
fe_CMYK.pack(side = LEFT)

lC = Label(fl_CMYK, text = "C", justify=LEFT)
lC.pack(side = TOP)
eC = Entry(fe_CMYK, width=8)
eC.pack(side = TOP)

lM = Label(fl_CMYK, text = "M", justify=LEFT)
lM.pack(side = TOP)
eM = Entry(fe_CMYK, width=8)
eM.pack(side = TOP)

lY = Label(fl_CMYK, text = "Y", justify=LEFT)
lY.pack(side = TOP)
eY = Entry(fe_CMYK, width=8)
eY.pack(side = TOP)

lK = Label(fl_CMYK, text = "K", justify=LEFT)
lK.pack(side = TOP)
eK = Entry(fe_CMYK, width=8)
eK.pack(side = TOP)

def er(event):
    s = eR.get()
    if (s.isdigit() or (s == '')):
        if (s == ''):
            return
        if(s.isdigit()):
            palette.red = int(s)
        if (int(s)>255):
            eR.insert(0, '0')
            palette.red = 0
    else:
        eR.insert(0, '0')
        palette.red = 0
    palette.transForRGB()
    b_colorchoser.config(bg = palette.s_color)
    resetValuesPalette()

def eg(event):
    s = eG.get()
    if (s.isdigit() or (s == '')):
        if (s == ''):
            return
        if (s.isdigit()):
            palette.green = int(s)
        if (int(s)>255):
            eG.insert(0, '0')
            palette.green = 0
    else:
        eG.insert(0, '0')
        palette.green = 0
    palette.transForRGB()
    b_colorchoser.config(bg = palette.s_color)
    resetValuesPalette()

def eb(event):
    s = eB.get()
    if (s.isdigit() or (s == '')):
        if (s == ''):
            return
        if (s.isdigit()):
            palette.blue = int(s)
        if (int(s)>255):
            eB.insert(0, '0')
            palette.blue = 0
    else:
        eB.insert(0, '0')
        palette.blue = 0
    palette.transForRGB()
    b_colorchoser.config(bg = palette.s_color)
    resetValuesPalette()

def eh(event):
    s = eH.get()
    if (s.isdigit() or (s == '')):
        if (s == ''):
            return
        if(s == ''):
            pass
        if(s.isdigit()):
            palette.hue = int(s)
        if (int(s)>360):
            eH.insert(0, '0')
            palette.hue = 0
    else:
        eH.insert(0, '0')
        palette.hue = 0
    palette.transForHSV()
    b_colorchoser.config(bg = palette.s_color)
    resetValuesPalette()

def es(event):
    s = eS.get()
    if (s.isdigit() or (s == '')):
        if (s == ''):
            return
        if(s.isdigit()):
            palette.saturation = int(s)
        if (int(s)>100):
            eS.insert(0, '0')
            palette.saturation = 0
    else:
        eS.insert(0, '0')
        palette.saturation = 0
    palette.transForHSV()
    b_colorchoser.config(bg = palette.s_color)
    resetValuesPalette()

def ev(event):
    s = eV.get()
    if (s.isdigit() or (s == '')):
        if (s == ''):
            return
        if(s.isdigit()):
            palette.value = int(s)
        if (int(s)>100):
            eV.insert(0, '0')
            palette.value = 0
    else:
        eV.insert(0, '0')
        palette.value = 0
    palette.transForHSV()
    b_colorchoser.config(bg = palette.s_color)
    resetValuesPalette()

def ec(event):
    s = eC.get()
    if (s.isdigit() or (s == '')):
        if (s == ''):
            return
        if(s.isdigit()):
            palette.c = int(s)
        if (int(s)>100):
            eC.insert(0, '0')
            palette.c = 0
    else:
        eC.insert(0, '0')
        palette.c = 0
    palette.transForCMYK()
    b_colorchoser.config(bg = palette.s_color)
    resetValuesPalette()

def em(event):
    s = eM.get()
    if (s.isdigit() or (s == '')):
        if (s == ''):
            return
        if(s.isdigit()):
            palette.m = int(s)
        if (int(s)>100):
            eM.insert(0, '0')
            palette.m = 0
    else:
        eM.insert(0, '0')
        palette.m = 0
    palette.transForCMYK()
    b_colorchoser.config(bg = palette.s_color)
    resetValuesPalette()

def ey(event):
    s = eY.get()
    if (s.isdigit() or (s == '')):
        if (s == ''):
            return
        if(s.isdigit()):
            palette.y = int(s)
        if (int(s)>100):
            eY.insert(0, '0')
            palette.y = 0
    else:
        eY.insert(0, '0')
        palette.y = 0
    palette.transForCMYK()
    b_colorchoser.config(bg = palette.s_color)
    resetValuesPalette()

def ek(event):
    s = eK.get()
    if (s.isdigit() or (s == '')):
        if (s == ''):
            return
        if(s.isdigit()):
            palette.k = int(s)
        if (int(s)>100):
            eK.insert(0, '0')
            palette.k = 0
    else:
        eK.insert(0, '0')
        palette.k = 0
    palette.transForCMYK()
    b_colorchoser.config(bg = palette.s_color)
    resetValuesPalette()

def ers(event):
    eR.delete(0, END)
def egs(event):
    eG.delete(0, END)
def ebs(event):
    eB.delete(0, END)
def ehs(event):
    eH.delete(0, END)
def ess(event):
    eS.delete(0, END)
def evs(event):
    eV.delete(0, END)
def ecs(event):
    eC.delete(0, END)
def ems(event):
    eM.delete(0, END)
def eys(event):
    eY.delete(0, END)
def eks(event):
    eK.delete(0, END)

def resetValuesPalette():
    eR.delete(0, END)
    eR.insert(0, str(palette.red))
    eG.delete(0, END)
    eG.insert(0, str(palette.green))
    eB.delete(0, END)
    eB.insert(0, str(palette.blue))
    eH.delete(0, END)
    eH.insert(0, str(palette.hue))
    eS.delete(0, END)
    eS.insert(0, str(palette.saturation))
    eV.delete(0, END)
    eV.insert(0, str(palette.value))
    eC.delete(0, END)
    eC.insert(0, str(palette.c))
    eM.delete(0, END)
    eM.insert(0, str(palette.m))
    eY.delete(0, END)
    eY.insert(0, str(palette.y))
    eK.delete(0, END)
    eK.insert(0, str(palette.k))



palette.define()
resetValuesPalette()


eR.bind("<KeyRelease>", er)
eR.bind("<FocusIn>", ers)
eG.bind("<KeyRelease>", eg)
eG.bind("<FocusIn>", egs)
eB.bind("<KeyRelease>", eb)
eB.bind("<FocusIn>", ebs)
eH.bind("<KeyRelease>", eh)
eH.bind("<FocusIn>", ehs)
eS.bind("<KeyRelease>", es)
eS.bind("<FocusIn>", ess)
eV.bind("<KeyRelease>", ev)
eV.bind("<FocusIn>", evs)
eC.bind("<KeyRelease>", ec)
eC.bind("<FocusIn>", ecs)
eM.bind("<KeyRelease>", em)
eM.bind("<FocusIn>", ems)
eY.bind("<KeyRelease>", ey)
eY.bind("<FocusIn>", eys)
eK.bind("<KeyRelease>", ek)
eK.bind("<FocusIn>", eks)

canvas.bind('<Motion>', logic.move)
canvas.bind('<B1-Motion>', logic.drag)
canvas.bind('<Button-1>', logic.click)
canvas.bind('<B1-Shift>')


window.mainloop()