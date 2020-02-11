from display import *


def draw_line(x0, y0, x1, y1, screen, color):
    if (x0 > x1):
        x0, y0, x1, y1 = x1, y1, x0, y0
    try:
        slope = (y1 - y0) / (x1 - x0)
        if (slope < 1):
            octant1(x0, y0, x1, y1, screen, color)
        elif (slope >= 1):
            octant2(x0, y0, x1, y1, screen, color)
        elif (slope <= -1):
            octant7(x0, y0, x1, y1, screen, color)
        else:
            octant8(x0, y0, x1, y1, screen, color)
    except ZeroDivisionError:
        while (y0 <= y1):
            plot(screen, color, int(x0), int(y0))
            y0 += 1


def octant1(x0, y0, x1, y1, screen, color):
    A = y1 - y0
    B = x1 - x0
    d = (2 * A) + B
    A *= 2
    B *= 2
    while (x0 <= x1):
        plot(screen, color, int(x0), int(y0))
        if (d > 0):
            y0 += 1
            d += B
        x0 += 1
        d += A


def octant2(x0, y0, x1, y1, screen, color):
    A = y1 - y0
    B = x1 - x0
    d = A + (2 * B)
    A *= 2
    B *= 2
    while (y0 <= y1):
        plot(screen, color, int(x0), int(y0))
        if (d < 0):
            x0 += 1
            d += A
        y0 += 1
        d += B


def octant7(x0, y0, x1, y1, screen, color):
    A = y1 - y0
    B = x1 - x0
    d = A - (2 * B)
    A *= 2
    B *= 2
    while (y0 >= y1):
        plot(screen, color, int(x0), int(y0))
        if (d > 0):
            x0 += 1
            d += A
        y0 -= 1
        d -= B


def octant8(x0, y0, x1, y1, screen, color):
    A = y1 - y0
    B = x1 - x0
    d = (2 * A) - B
    A *= 2
    B *= 2
    while (x0 <= x1):
        plot(screen, color, int(x0), int(y0))
        if (d < 0):
            y0 -= 1
            d -= B
        x0 += 1
        d += A
