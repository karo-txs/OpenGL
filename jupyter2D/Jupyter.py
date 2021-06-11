import math
from OpenGL.GL import *


class Jupyter:
    def draw_jupyter(self, x, y):
        triangleAmount = 100

        glBegin(GL_TRIANGLE_FAN)
        glVertex2f(x, y)
        for i in range(int(triangleAmount / 2)):
            glColor3f(230/255, 182/255, 126/255)
            glVertex2f(
                x + (2 * math.cos(i * (2.3 * math.pi) / triangleAmount)),
                y + (2 * math.sin(i * (2.3 * math.pi) / triangleAmount))
            )
        for i in range(int(triangleAmount / 2), triangleAmount):
            glColor3f(126/255, 107/255, 86/255)

            glVertex2f(
                x + (2 * math.cos(i * (2.3 * math.pi) / triangleAmount)),
                y + (2 * math.sin(i * (2.3 * math.pi) / triangleAmount))
            )
        glEnd()

    def draw_jupyter_matrix(self, boxx, boxy):
        glPushMatrix()
        glTranslatef(0, 0, -10)
        glTranslatef(boxx, boxy, 0)
        self.draw_jupyter(-20, 0)
        glPopMatrix()

