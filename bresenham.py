import sys
import math

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

WIDTH, HEIGHT = 600, 600
CENTER_Y, CENTER_X = HEIGHT // 2, WIDTH //2
RADIUS_Y, RADIUS_X = 100, 200
GREEN = (0.0, 1.0, 0.0)

def draw_bresenham_ellipse():
    x, y = 0, RADIUS_Y
    dx, dy = 0, 2 * RADIUS_X * RADIUS_X * y
    d1, d2 = RADIUS_Y * RADIUS_Y - (RADIUS_X * RADIUS_X * RADIUS_Y) + (0.25 * RADIUS_X * RADIUS_X), 0

    while dx < dy:
        glVertex2f(x + CENTER_X, y + CENTER_Y)
        glVertex2f(-x + CENTER_X, y + CENTER_Y)
        glVertex2f(x + CENTER_X, -y + CENTER_Y)
        glVertex2f(-x + CENTER_X, -y + CENTER_Y)

        if d1 < 0:
            x += 1
            dx += 2 * RADIUS_Y * RADIUS_Y
            d1 += dx + RADIUS_Y * RADIUS_Y
        else:
            x += 1
            y -= 1
            dx += 2 * RADIUS_Y * RADIUS_Y
            dy -= 2 * RADIUS_X * RADIUS_X
            d1 += dx - dy + RADIUS_Y * RADIUS_Y

        glVertex2f(x + CENTER_X, y + CENTER_Y)
        glVertex2f(-x + CENTER_X, y + CENTER_Y)
        glVertex2f(x + CENTER_X, -y + CENTER_Y)
        glVertex2f(-x + CENTER_X, -y + CENTER_Y)

    d2 = (RADIUS_Y * RADIUS_Y * (x + 0.5) * (x + 0.5)) + \
         (RADIUS_X * RADIUS_X * (y - 1) * (y - 1)) - \
         (RADIUS_X * RADIUS_X * RADIUS_Y * RADIUS_Y)

    while y >= 0:
        glVertex2f(x + CENTER_X, y + CENTER_Y)
        glVertex2f(-x + CENTER_X, y + CENTER_Y)
        glVertex2f(x + CENTER_X, -y + CENTER_Y)
        glVertex2f(-x + CENTER_X, -y + CENTER_Y)

        if d2 > 0:
            y -= 1
            dy -= 2 * RADIUS_X * RADIUS_X
            d2 += RADIUS_X * RADIUS_X - dy
        else:
            x += 1
            y -= 1
            dx += 2 * RADIUS_Y * RADIUS_Y
            dy -= 2 * RADIUS_X * RADIUS_X
            d2 += dx - dy + RADIUS_X * RADIUS_X

def draw():
    glClear(GL_COLOR_BUFFER_BIT)
    glBegin(GL_POINTS)
    glColor3f(*GREEN)
    
    
    draw_bresenham_ellipse() 
    glEnd()
    glFlush()

def initialize():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(WIDTH, HEIGHT)
    glutCreateWindow("Ellipse Drawing")
    gluOrtho2D(0, WIDTH, 0, HEIGHT)
    glClearColor(0.0, 0.0, 0.0, 1.0)

def main():
    initialize()
    glutDisplayFunc(draw)
    glutMainLoop()

if __name__ == "__main__":
    main()