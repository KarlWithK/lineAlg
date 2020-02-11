from display import *


def draw_line(x0, y0, x1, y1, screen, color):
    if (x0 > x1):
        x0, y0, x1, y1 = x1, y1, x0, y0
    try:
        slope = (y1 - y0) / (x1 - x0)
        if (0 <= slope < 1):
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
    B = -1 * (x1 - x0)
    D = (2 * A) + B
    A *= 2
    B *= 2
    while (x0 <= x1):
        plot(screen, color, int(x0), int(y0))
        if (D > 0):
            y0 += 1
            D += B
        x0 += 1
        D += A


def octant2(x0, y0, x1, y1, screen, color):
    A = y1 - y0
    B = -1 * (x1 - x0)
    D = A + (2 * B)
    A *= 2
    B *= 2
    while (y0 <= y1):
        plot(screen, color, int(x0), int(y0))
        if (D < 0):
            x0 += 1
            D += A
        y0 += 1
        D += B


def octant7(x0, y0, x1, y1, screen, color):
    A = y1 - y0
    B = -1 * (x1 - x0)
    D = A - (2 * B)
    A *= 2
    B *= 2
    while (y0 >= y1):
        plot(screen, color, int(x0), int(y0))
        if (D > 0):
            x0 += 1
            D += A
        y0 -= 1
        D -= B


def octant8(x0, y0, x1, y1, screen, color):
    A = y1 - y0
    B = -1 * (x1 - x0)
    D = (2 * A) - B
    A *= 2
    B *= 2
    while (x0 <= x1):
        plot(screen, color, int(x0), int(y0))
        if (D < 0):
            y0 -= 1
            D -= B
        x0 += 1
        D += A


def draw_line_one(x0, y0, x1, y1, screen, color):
    if (x0 > x1):
        x0, y0, x1, y1 = x1, y1, x0, y0
    try:
        slope = (y1 - y0) / (x1 - x0)
        A = y1 - y0
        B = -1 * (x1 - x0)
        if (0 <= slope < 1):
            D = (2 * A) + B
            A *= 2
            B *= 2
            while (x0 <= x1):
                plot(screen, color, int(x0), int(y0))
                if (D > 0):
                    y0 += 1
                    D += B
                x0 += 1
                D += A
        elif (slope >= 1):
            D = A + (2 * B)
            A *= 2
            B *= 2
            while (y0 <= y1):
                plot(screen, color, int(x0), int(y0))
                if (D < 0):
                    x0 += 1
                    D += A
                y0 += 1
                D += B
        elif (slope <= -1):
            D = A - (2 * B)
            A *= 2
            B *= 2
            while (y0 >= y1):
                plot(screen, color, int(x0), int(y0))
                if (D > 0):
                    x0 += 1
                    D += A
                y0 -= 1
                D -= B
        else:
            D = (2 * A) - B
            A *= 2
            B *= 2
            while (x0 <= x1):
                plot(screen, color, int(x0), int(y0))
                if (D < 0):
                    y0 -= 1
                    D -= B
                x0 += 1
            D += A
    except ZeroDivisionError:
        while (y0 <= y1):
            plot(screen, color, int(x0), int(y0))
            y0 += 1
