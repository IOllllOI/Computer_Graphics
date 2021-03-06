from threading import Thread, Lock
from time import sleep
import algorithms
import math

lock = Lock()
st = False

def returnS():
    for j in range(len(shapes)):
        shapes[j].draw()

def rotation():
    copyShapes = []
    while True:
        angle = 0
        for i in range(180):
            lock.acquire()
            if st is True:
                break
            lock.release()

            angle += math.pi/60
            c_clear()
            copyShapes.clear()
            for j in range(len(shapes)):
                point = algorithms.Point2d(shapes[j].x, shapes[j].y)
                copyShapes.append(point)

            for j in range(len(copyShapes)):
                copyShapes[j].rotation(angle)
                copyShapes[j].draw()
            # sleep(0.1)





shapes = []

widthInPix = 3

c_clear = lambda: 0
def delete_shapes():
    shapes.clear()

set_coordinats = lambda x, y: 0

px = 0
py = 0

count_click = 0

center = algorithms.Point(0, 0)
th_list = []

def rotarion_radio_b():
    global th_list
    global count_click
    global st
    if count_click == 0:
        st = False
        th_list.clear()
        th_list.append(Thread(target=rotation, daemon=True))
        th_list[0].start()
        count_click = 1
    else:
        lock.acquire()
        st = True
        lock.release()
        count_click = 0
        print(count_click)


def move(event):
    x = event.x
    y = event.y
    set_coordinats(x, y)



def drag(event):

    x = event.x
    y = event.y
    set_coordinats(x, y)
    global px
    global py
    sign = 1
    cx = algorithms.cx
    cy = algorithms.cy


    point = algorithms.Point2d(x, y)
    shapes.append(point)
    point.draw()



def click(event):
    x = event.x
    y = event.y

    point = algorithms.Point2d(x, y)
    shapes.append(point)
    point.draw()





