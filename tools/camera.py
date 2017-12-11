from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from math import pow, sqrt, pi, acos, cos, sin


class Camera:
    def __init__(self):
        self.x = 4
        self.y = 0
        self.z = 1
        self.lx = 0
        self.ly = 0
        self.lz = 0
        self.speed = 0.1
        self.speedAngle = 0.05

    def move(self, deltaX, deltaY, deltaZ):
        rayon = sqrt(pow(self.x - self.lx, 2) + pow(self.y - self.ly, 2) + pow(self.z - self.lz, 2))
        angleX = acos((self.x - self.lx) / rayon)
        angleY = acos((self.y - self.ly) / rayon) - pi / 2
        angleZ = acos((self.z - self.lz) / rayon)

        if angleZ < pi / 2:
            angleX = -angleX
        if abs(angleX) > pi / 2:
            angleZ = -angleZ

        if angleX > pi / 2:
            deltaAngleX = 2 * (pi - angleX) / pi
        elif angleX < - pi / 2:
            deltaAngleX = 2 * (-pi - angleX) / pi
        else:
            deltaAngleX = 2 * angleX / pi

        if angleZ > pi / 2:
            deltaAngleZ = 2 * (pi - angleZ) / pi
        elif angleZ < - pi / 2:
            deltaAngleZ = 2 * (-pi - angleZ) / pi
        else:
            deltaAngleZ = 2 * angleZ / pi
        deltaAngleY = 2 * angleY / pi

        self.x += deltaX * self.speed * deltaAngleX - deltaZ * self.speed * deltaAngleZ
        self.lx += deltaX * self.speed * deltaAngleX - deltaZ * self.speed * deltaAngleZ
        self.y += deltaY * self.speed - deltaZ * self.speed * deltaAngleY 
        self.ly += deltaY * self.speed - deltaZ * self.speed * deltaAngleY 
        self.z += deltaZ * self.speed * deltaAngleX + deltaX * self.speed * deltaAngleZ
        self.lz += deltaZ * self.speed * deltaAngleX + deltaX * self.speed * deltaAngleZ

    def lookAt(self, deltaAngleX, deltaAngleY):
        rayon = round(sqrt(pow(self.x - self.lx, 2) + pow(self.y - self.ly, 2) + pow(self.z - self.lz, 2)), 2)
        angleX = acos((self.x - self.lx) / rayon)
        angleY = acos((self.y - self.ly) / rayon) - pi / 2

        print("Distance camera-view : ", rayon)
        print("AngleX : ", angleX)
        print("AngleY : ", angleY)

        self.lx = self.x + rayon * cos(angleX)
        self.lz = self.z + rayon * sin(angleX)

    def update(self, keys_pressed):
        if keys_pressed != {}:
            print(keys_pressed)
        if b'r' in keys_pressed or b'R' in keys_pressed:
            self.__init__()
            return
        if GLUT_KEY_LEFT in keys_pressed:
            self.move(1, 0, 0)
        if GLUT_KEY_UP in keys_pressed:
            self.move(0, 0, 1)
        if GLUT_KEY_RIGHT in keys_pressed:
            self.move(-1, 0, 0)
        if GLUT_KEY_DOWN in keys_pressed:
            self.move(0, 0, -1)
        if 112 in keys_pressed:
            self.move(0, 1, 0)
        if 114 in keys_pressed:
            self.move(0, -1, 0)

    def hud(self):
        def text_ui(text, x, y):
            glColor3f(1,1,1)
            glWindowPos2s(x,y);
            for i in text:
                glutBitmapCharacter(GLUT_BITMAP_9_BY_15, ord(i))

        text_ui("Camera: {}, {}, {}".format(round(self.x, 2), round(self.y, 2), round(self.z, 2)), 10, glutGet(GLUT_WINDOW_HEIGHT) - 20)
        text_ui("View: {}, {}, {}".format(round(self.lx, 2), round(self.ly, 2), round(self.lz, 2)), 10, glutGet(GLUT_WINDOW_HEIGHT) - 35)

    def draw(self):
        # gluLookAt(self.x, self.y, self.z, self.lx, self.ly, self.lz, 0, 1, 0)
        gluLookAt(0.0000000001,20,0,0,0,0,0,1,0)
