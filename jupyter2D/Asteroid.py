import math
from OpenGL.GL import *


class Asteroid:
    def __init__(self):
        self.x = -1
        self.y = -1

    def draw_asteroid(self, x, y):
        # r = 2
        # num_segments = 30
        # glBegin(GL_LINE_LOOP)
        # glColor3f(0.75, 0.54, 0.33)
        # for i in range(num_segments):
        #     theta = 2.0 * math.pi * i / num_segments
        #     x = r * math.cos(theta)
        #     y = r * math.sin(theta)
        #     glVertex2f(x + cx, y + cy)
        # glEnd()

        triangleAmount = 100

        glBegin(GL_TRIANGLE_FAN)
        glVertex2f(x, y)
        for i in range(int(triangleAmount / 2)):
            glColor3f(75 / 255, 54 / 255, 33 / 255)
            glVertex2f(
                x + (2 * math.cos(i * (2.3 * math.pi) / triangleAmount)),
                y + (2 * math.sin(i * (2.3 * math.pi) / triangleAmount))
            )
        for i in range(int(triangleAmount / 2), triangleAmount):
            glColor3f(85 / 255, 64 / 255, 43 / 255)

            glVertex2f(
                x + (2 * math.cos(i * (2.3 * math.pi) / triangleAmount)),
                y + (2 * math.sin(i * (2.3 * math.pi) / triangleAmount))
            )
        glEnd()

    def draw_asteroid_matrix(self, x, y, tam):
        if self.x == -1 and self.y == -1:
            self.x = x
            self.y = y

        glPushMatrix()
        glTranslatef(0, 0, -tam)
        # if self.pos <= -50:
        #     self.pos = 100
        # else:
        #     self.pos -= 0.5
        self.x -= 0.5
        glTranslatef(self.x, 0, 0)
        self.draw_asteroid(self.x, self.y)
        glPopMatrix()