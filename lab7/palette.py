

s_color = "#ffffff"
curr_color = "#000000"

def changeColor():
    global curr_color
    curr_color = s_color

# диапазоны RGB
# R - (0; 255)
# G - (0; 255)
# B - (0; 255)
red = 0
green = 0
blue = 0
# диапазоны HSV
# H - (0;360)
# S - (0;100)
# V - (0;100)
hue = 0
saturation = 0
value = 0
# диапазоны C/M/Y/K = (0;100)
c = 0
m = 0
y = 0
k = 0

def define():
    transForRGB()

def setColor():
    global s_color
    r = hex(red)
    g = hex(green)
    b = hex(blue)
    s_color = '#'
    if red < 16:
        s_color += '0'
    for i in range(2,len(r)):
        s_color += r[i]
    if green < 16:
        s_color += '0'
    for i in range(2,len(g)):
        s_color += g[i]
    if blue < 16:
        s_color += '0'
    for i in range(2,len(b)):
        s_color += b[i]

    print(s_color)


def RGBtoHSV():
    global hue, saturation, value
    # RGB to HSV
    # определение яркости
    if(red == 0) or (green == 0) or (blue == 0):
        hue = 0
        saturation = 0
        value = 0
        return
    value = max(red, green, blue)
    temp = min(red, green, blue)
    # определения насыщенности
    if value == 0:
        saturation = 0
    else:
        saturation = round((value - temp) / value * 100)

    # Определениие тона
    if value == temp:
        hue = 0
        return
    if value == blue:
        hue = round(60 * (red - green) / (value - temp) + 240)
    if value == green:
        hue = round(60 * (blue - red) / (value - temp) + 120)
    if (value == red) and (green < blue):
        hue = round(60 * (green - blue) / (value - temp) + 360)
    if (value == red) and (green >= blue):
        hue = round(60 * (green - blue) / (value - temp))
    value = round(value/2.55)

def RGBtoCMYK():
    global c, m, y, k

    # RGB to CMYK
    r = red / 2.55
    g = green / 2.55
    b = blue / 2.55
    C = 0
    M = 0
    Y = 0
    K = 0

    K = 100 - max(r, g, b)
    if (red != 0) or (green != 0) or (blue != 0):
        C = (100 - r - K) / (100 - K)
        M = (100 - g - K) / (100 - K)
        Y = (100 - b - K) / (100 - K)
    else:
        C = 0
        M = 0
        Y = 0
    c = round(C*100)
    m = round(M*100)
    y = round(Y*100)
    k = round(K)



def HSVtoRGB():
    global red, green, blue
    # HSV to RGB
    hi = round(hue / 60)
    #
    c = (value/100) * (saturation/100)
    x = c * (1 - abs((hue/60) % 2 - 1))
    m = (value/100) - c
    r = 0
    g = 0
    b = 0
    if hi == 0:
        r = c
        g = x
        b = 0
    if hi == 1:
        r = x
        g = c
        b = 0
    if hi == 2:
        r = 0
        g = c
        b = x
    if hi == 3:
        r = 0
        g = x
        b = c
    if hi == 4:
        r = x
        g = 0
        b = c
    if hi >= 5:
        r = c
        g = 0
        b = x

    red = round((r + m) * 255)
    green = round((g + m) * 255)
    blue = round((b + m) * 255)

def CMYKtoRGB():
    global red, green, blue

    red = round((2.55 * (100 - c) * (100 - k))/100)
    green = round((2.55 * (100 - m) * (100 - k))/100)
    blue = round((2.55 * (100 - y) * (100 - k))/100)


def transForRGB():
    RGBtoCMYK()
    RGBtoHSV()
    setColor()

def transForHSV():
    HSVtoRGB()
    RGBtoCMYK()
    setColor()

def transForCMYK():
    CMYKtoRGB()
    RGBtoHSV()
    setColor()



