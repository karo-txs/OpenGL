import math
from OpenGL.GL import *


class Star:
    def draw_star(self, x, y, t):

        glBegin(GL_TRIANGLES)
        glColor3f(1, 1, 1)
        if t % 10 == 0:
            glColor3f(1, abs(math.cos(t)), abs(math.sin(t)))
        glVertex3f(x[0], y[0], 0)
        glVertex3f(x[1], y[1], 0)
        glVertex3f(x[2], y[2], 0)
        glEnd()

    def draw_star_matrix(self, pos_stars_x, pos_stars_y, t):
        glPushMatrix()

        glTranslatef(0, 0, -90)

        x1, x2, x3 = 2, 4, 3
        y1, y2, y3 = 0, 0, 2

        for x, y in zip(pos_stars_x, pos_stars_y):
            self.draw_star([x1+x, x2+x, x3+x], [y1 + y, y2 + y, y3 + y], t)
            self.draw_star([x1+x, x2+x, x3+x], [y1 + y + 1.5, y2 + y + 1.5, y3 + y - 2.5], t)

        glPopMatrix()

