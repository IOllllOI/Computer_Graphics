import algorithms

shapes = []

widthInPix = 1

c_clear = lambda: 0
set_coordinats = lambda x, y: 0

i_shape = 0
def change_shape(number):
    global i_shape
    i_shape = number

i_operating_mode = 0
def change_mode(number):
    global i_operating_mode
    i_operating_mode = number

x_begin = 0
y_begin = 0

count_click = 0

def select_draw():
    change_mode(0)
    global count_click
    count_click = 0
    c_clear()

def select_demonstration():
    change_mode(1)
    global count_click
    count_click = 0
    c_clear()

def c_pencil():
    change_shape(0)
    global count_click
    count_click = 0
    if i_operating_mode == 1:
        c_clear()

def c_line():
    change_shape(1)
    global count_click
    count_click = 0
    if i_operating_mode == 1:
        c_clear()

def c_circle():
    change_shape(2)
    global count_click
    count_click = 0
    if i_operating_mode == 1:
        c_clear()

def c_ellipse():
    change_shape(3)
    global count_click
    count_click = 0
    if i_operating_mode == 1:
        c_clear()

def move(event):
    x = event.x
    y = event.y
    set_coordinats(x, y)

def drag(event):
    x = event.x
    y = event.y
    set_coordinats(x, y)
    global i_shape
    global i_operating_mode

    if i_shape == 0:
        point = algorithms.Point2d(x, y)
        shapes.append(point)
        point.draw()

    if i_operating_mode == 1:

        global x_begin
        global y_begin
        global x_end
        global y_end
        if i_shape == 1:
            c_clear()
            x_end = x
            y_end = y
            line = algorithms.Line(x_begin, y_begin, x_end, y_end)
            line.draw()

        if i_shape == 2:
            c_clear()
            x_end = x
            y_end = y
            radius = int((pow(abs(x_begin - x_end), 2) +
                pow(abs(y_begin - y_end), 2)) ** (1 / 2))
            circle = algorithms.Circle(x_begin, y_begin, radius)
            circle.draw()

        if i_shape == 3:
            c_clear()
            x_end = x
            y_end = y
            a = int(abs(x_begin - x_end))
            b = int(abs(y_begin - y_end))
            ellipse = algorithms.Ellipse(x_begin, y_begin, a, b)
            ellipse.draw()





def click(event):
    x = event.x
    y = event.y
    i = 0
    x_end = 0
    y_end = 0
    global x_begin
    global y_begin
    global i_operating_mode
    if i_operating_mode == 0:
        global i_shape
        global count_click



        if i_shape == 0:
            point = algorithms.Point2d(x, y)
            shapes.append(point)
            point.draw()

        if i_shape == 1:
            if count_click == 0:
                x_begin = x
                y_begin = y
                i = 1

            if count_click == 1:
                x_end = x
                y_end = y
                line = algorithms.Line(x_begin, y_begin, x_end, y_end)
                shapes.append(line)
                line.draw()
                i = 0
        if i_shape == 2:
            if count_click == 0:
                x_begin = x
                y_begin = y
                i = 1

            if count_click == 1:
                x_end = x
                y_end = y
                radius = int((pow(abs(x_begin - x_end), 2) +
                              pow(abs(y_begin - y_end), 2)) ** (1/2))
                circle = algorithms.Circle(x_begin, y_begin, radius)
                shapes.append(circle)
                circle.draw()
                i = 0
        if i_shape == 3:
            if count_click == 0:
                x_begin = x
                y_begin = y
                i = 1

            if count_click == 1:
                x_end = x
                y_end = y
                a = int(abs(x_begin - x_end))
                b = int(abs(y_begin - y_end))
                ellipse = algorithms.Ellipse(x_begin, y_begin, a, b)
                shapes.append(ellipse)
                ellipse.draw()
                i = 0
        count_click = i
    if i_operating_mode == 1:
        x_begin = x
        y_begin = y

def come_back():
    for i in range(len(shapes)):
        shapes[i].draw()
