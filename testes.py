import pygame
import sys
import math
import pygame.draw
import time
from OpenGL.GL import *
from OpenGL.GLU import *

if __name__ == '__main__':
    pygame.init()

    size = (800, 1000)
    black = (0, 0, 0)
    white = (255, 255, 255)

    phi = 0.0
    theta = 75.0
    delta_angle = 10.0
    boxy = 0

    screen = pygame.display.set_mode(size, pygame.OPENGL | pygame.DOUBLEBUF)

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()

    gluPerspective(100, 3.0 / 4.0, 10, 1000)
    glMatrixMode(GL_MODELVIEW)

    x = 100.0
    y = 430.0
    t = 0
    vx = 0.0
    vy = 00.0

    def mod(x, y):
        res = x
        while res > y:
            res -= y
        return res


    def looparound(x):
        if x < 20:
            return x
        elif x > 20:
            return mod(x, 20)
        else:
            return -10


    def update():
        global x, y, vx, vy
        ax = 300.0 - x
        ay = 400.0 - y

        vx += 0.001 * ax
        vy += 0.001 * ay

        x += vx
        y += vy


    def draw_cube():
        glBegin(GL_QUADS)
        glColor3f(1, abs(math.cos(t)), abs(math.sin(t)))
        glVertex3f(-10, 0, 0)
        glVertex3f(-8, 0, 0)
        glVertex3f(-8, 2, 0)
        glVertex3f(-10, 2, 0)
        glEnd()

    def draw_retangle():
        glBegin(GL_POLYGON)
        glColor3f(0.5, 0.5, 1)
        #glColor3f(1, abs(math.cos(t)), abs(math.sin(t)))
        glVertex3f(-13, -2, 0)
        glVertex3f(-9, -2, 0)
        glVertex3f(-9, 0, 0)
        glVertex3f(-13, 0, 0)
        glEnd()

    def draw_triangle():
        glBegin(GL_TRIANGLES)
        glColor3f(0.5, 0.5, 1)
        glVertex3f(-13, 6, 0)
        # glVertex3f(7.5, 2, 0)
        # glVertex3f(9.5, 2, 0)
        glVertex3f(-10, 7, 0)
        glVertex3f(-10, 0, 0)
        glEnd()

    def draw_circle(x, y):
        triangleAmount = 100

        glBegin(GL_TRIANGLE_FAN)

        glVertex2f(x, y)
        for i in range(int(triangleAmount / 2)):
            glColor3f(0.75, 0.54, 0.33)
            glVertex2f(
                x + (2 * math.cos(i * (2.3 * math.pi) / triangleAmount)),
                y + (2 * math.sin(i * (2.3 * math.pi) / triangleAmount))
            )
        for i in range(int(triangleAmount / 2), triangleAmount):
            glColor3f(0.75, 0.54, 1)
            glVertex2f(
                x + (2 * math.cos(i * (2.3 * math.pi) / triangleAmount)),
                y + (2 * math.sin(i * (2.3 * math.pi) / triangleAmount))
            )
        glEnd()

    def draw_circle2(cx, cy):
        r = 2
        num_segments = 30
        glBegin(GL_LINE_LOOP)
        for i in range(num_segments):
            theta = 2.0 * math.pi * i / num_segments
            x = r * math.cos(theta)
            y = r * math.sin(theta)
            glVertex2f(x + cx, y + cy)
        glEnd()

    def draw_elipse(xr, yr):
        segments = 100
        angle = 0
        glBegin(GL_LINE_STRIP)
        glColor3f(1, 1, 1)
        while angle <= 2*math.pi:
            x = math.cos(angle) * xr
            y = math.sin(angle) * yr
            glVertex3f(x, y, 0)
            angle += 2*math.pi/segments
        glEnd()

    def draw():
        print()
        looparound(t), t
        glPushMatrix()
        glTranslatef(0, 0, -10)
        glTranslatef(looparound(t), boxy, 0)
        #glRotatef(t, 0, 1, 0)

        #draw_cube()
        #draw_triangle()
        draw_circle(0, 0)
        #draw_retangle()
        #draw_elipse(2, 1)
        draw_elipse(3, 0.5)
        glPopMatrix()

    while True:
        t += 1
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                sys.exit()
            elif ev.type == pygame.KEYDOWN:
                if (ev.key == pygame.K_ESCAPE or
                        ev.key == pygame.K_q):
                    draw()
                elif ev.key == pygame.K_UP:
                    boxy += 5
                    draw()
                elif ev.key == pygame.K_DOWN:
                    boxy -= 5
                    draw()

        update()
        glClearColor(0.0, 0.0, 0.0, 1.0)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        draw()

        pygame.display.flip()
        time.sleep(0.15)

