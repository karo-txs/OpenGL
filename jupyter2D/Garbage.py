from OpenGL.GL import *


class Garbage:
    def __init__(self):
        self.x = -1
        self.y = -1

    def draw_garbage(self, x, y):
        glBegin(GL_QUADS)
        glColor3f(0.5, 0.5, 0.5)
        glVertex3f(x[0], y[0], 0)
        glVertex3f(x[1], y[1], 0)
        glVertex3f(x[2], y[2], 0)
        glVertex3f(x[3], y[3], 0)
        glEnd()

    def draw_garbage2(self, x, y):
        glBegin(GL_POLYGON)
        glColor3f(0.5, 0.5, 0.5)
        glVertex3f(x[0], y[0], 0)
        glVertex3f(x[1], y[1], 0)
        glVertex3f(x[2], y[2], 0)
        glVertex3f(x[3], y[3], 0)
        glEnd()

    def draw_garbage_matrix(self, x, y, tam):
        if self.x == -1 and self.y == -1:
            self.x = x
            self.y = y

        glPushMatrix()
        glTranslatef(0, 0, -tam)
        self.x -= 0.1
        glTranslatef(self.x, 0, 0)
        self.draw_garbage([self.x, self.x - 2, self.x - 2, self.x], [y, y, y + 2, y + 2])
        self.draw_garbage2([self.x + 10, self.x + 6, self.x + 6, self.x + 10], [y + 6, y + 6, y + 4, y + 4])
        glPopMatrix()

