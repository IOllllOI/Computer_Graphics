


dpf = lambda x, y: 0

def brezenhem(x, y, anx, any, sx, sy):
    f = 0
    l = 0
    if anx > any:

        f = 2 * any - anx
        l = anx
        dpf(x, y)
        for i in range(l):
            if f >= 0:
                x += sx
                y += sy
                f += 2 * (any - anx)
            else:
                x += sx
                f += 2 * any
            dpf(x, y)
    else:

        f = 2 * anx - any
        l = any
        dpf(x, y)
        for i in range(l):
            if f >= 0:
                x += sx
                y += sy
                f += 2 * (anx - any)
            else:
                y += sy
                f += 2 * anx
            dpf(x, y)

class Point2d(object):

    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def draw(self):
        dpf(self.x, self.y)

class Line(object):

    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def draw(self):
        nx = self.x2 - self.x1
        ny = self.y2 - self.y1
        anx = abs(nx)
        any = abs(ny)
        sx = 1
        sy = 1

        if (nx < 0) and (ny > 0):
            sx = -1
            brezenhem(self.x1, self.y1, anx, any, sx,  sy)
        if (nx > 0) and (ny < 0):
            sy = -1
            brezenhem(self.x1, self.y1, anx, any, sx,  sy)
        if (nx < 0) and (ny < 0):
            sx = -1
            sy = -1
            brezenhem(self.x1, self.y1, anx, any, sx, sy)
        if (nx > 0) and (ny > 0):
            brezenhem(self.x1, self.y1, anx, any, sx, sy)

class  Circle(object):
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius

    def draw(self):
        d = 3 - 2 * self.radius
        u = 6
        v = 10 - 4 * self.radius
        x = 0
        y = self.radius
        while v < 10:
            dpf(self.x + x, self.y - y)
            dpf(self.x + y, self.y - x)
            dpf(self.x + y, self.y + x)
            dpf(self.x + x, self.y + y)
            dpf(self.x - x, self.y + y)
            dpf(self.x - y, self.y + x)
            dpf(self.x - y, self.y - x)
            dpf(self.x - x, self.y - y)
            if d < 10:
                d += u
                u += 4
                v += 4
                x += 1
            else:
                d += v
                u += 4
                v += 8
                x += 1
                y -= 1

class Ellipse(object):

    def __init__(self, x, y, a, b):
        self.x = x
        self.y = y
        self.a = a
        self.b = b

    def draw(self):
        x = 0
        y = self.b
        a_sqr = self.a ** 2
        b_sqr = self.b ** 2
        d = 4 * b_sqr * ((x + 1) ** 2) + a_sqr * ((2 * y - 1) ** 2) \
            - 4 * a_sqr * b_sqr

        while (a_sqr * (2 * y - 1)) > (2 * b_sqr * (x + 1)):
            dpf(self.x + x, self.y + y)
            dpf(self.x + x, self.y - y)
            dpf(self.x - x, self.y - y)
            dpf(self.x - x, self.y + y)
            if d < 0:
                x += 1
                d += 4 * b_sqr * (2 * x + 3)
            else:
                x += 1
                d -= 8 * a_sqr * (y - 1) - 4 * b_sqr * (2 * x + 3)
                y -= 1
        d = b_sqr * ((2 * x + 1) ** 2) + 4 * a_sqr * ((y + 1) ** 2) \
            - 4 * a_sqr * b_sqr
        while (y + 1) != 0:
            dpf(self.x + x, self.y + y)
            dpf(self.x + x, self.y - y)
            dpf(self.x - x, self.y - y)
            dpf(self.x - x, self.y + y)
            if d < 0:
                y -= 1
                d += 4 * a_sqr * (2 * y + 3)
            else:
                y -= 1
                d -= 8 * b_sqr * (x + 1) - 4 * a_sqr * (2 * y + 3)
                x += 1
