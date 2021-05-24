import math
import numpy as np
from tkinter import *

root = Tk()
root.title('Лабораторная №6')
c = Canvas(root, width=700, height=700, bg='yellow')
c.pack()

rad = 0
arrR = []


def redraw(rad):
    i = 0
    alpha1 = -math.pi / 90
    alpha = math.pi / 90

    aa = -250
    bb = 250
    tmp = np.array([[bb, aa, aa, 1],
                    [bb, bb, aa, 1],
                    [aa, aa, aa, 1],
                    [aa, bb, aa, 1],
                    [bb, aa, bb, 1],
                    [bb, bb, bb, 1],
                    [aa, aa, bb, 1],
                    [aa, bb, bb, 1]])

    while 1:
        coord = tmp.copy()

        m0 = np.array([[np.cos(alpha), 0, np.sin(alpha), 0],  # OY
                       [0, 1, 0, 0],
                       [-np.sin(alpha), 0, np.cos(alpha), 0],
                       [0, 0, 0, 1]])
        for i in range(8):
            coord[i, :] = np.dot(coord[i, :], m0)

        r = 10000000

        tetta = math.pi / 4
        fi = math.pi / 4
        x = r * math.sin(fi) * math.cos(tetta)
        y = r * math.sin(fi) * math.sin(tetta)
        z = r * math.sin(fi)
        coordE = np.array([0, 0, 0])
        arrE = []
        arrL2 = []

        points2 = []
        coordE2 = []
        points = []
        arrV = np.array([[-math.sin(tetta), -math.cos(fi) * np.cos(tetta), -math.sin(fi) * math.cos(tetta), 0],
                         [math.cos(tetta), -math.cos(fi) * math.sin(tetta), -math.sin(fi) * math.sin(tetta), 0],
                         [0, math.sin(fi), -math.cos(fi), 0],
                         [0, 0, r, 1]])
        for i in range(8):
            arr = np.array(coord[i, :])
            arrE.append(np.dot(arr, arrV))

        arrE = np.array(arrE)

        for i in range(8):
            arr2 = np.array(arrE[i, :3:])
            arrL2.append(list(arr2))

        for el in arrL2:
            coordE2.append([(((r / 2) * el[0]) / el[2]), (((r / 2) * el[1]) / el[2])])
        for el in coordE2:
            for i in el:
                points.append(i + 350)

        cube = c.create_line(points[8], points[9], points[10], points[11], points[14], points[15], points[12],
                             points[13],
                             points[8], points[9], points[0], points[1], points[2], points[3], points[10], points[11],
                             points[2], points[3], points[6], points[7], points[14], points[15], points[6], points[7],
                             points[4], points[5], points[12], points[13], points[4], points[5], points[0], points[1], width = 5 )

        root.after(30)
        root.update()
        c.pack()
        c.delete(ALL)
        alpha += alpha1


redraw(rad)
root.mainloop()