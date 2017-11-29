from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from math import pow, sqrt, degrees, pi, acos, cos, sin


class Camera:
    def __init__(self):
        self.x = 5
        self.y = 1
        self.z = -5
        self.lx = 0
        self.ly = 0
        self.lz = 0
        self.speed = 0.1
        self.speedAngle = 0.05

    def move(self, deltaX, deltaY, deltaZ):
        if pow(self.x - self.lx, 2) + pow(self.z - self.lz, 2) != 0:
            angleX = (abs(self.x - self.lx) / sqrt(pow(self.z - self.lz, 2) + pow(self.x - self.lx, 2)))
        else:
            angleX = 0
        if pow(self.y - self.ly, 2) + pow(self.z - self.lz, 2) != 0:
            angleY = (abs(self.x - self.lx) / sqrt(pow(self.y - self.ly, 2) + pow(self.x - self.lx, 2)))
        else:
            angleY = 0
        deltaAngleX = acos(angleX) / pi * 2
        deltaAngleY = acos(angleY) / pi * 2
        self.x += deltaX * self.speed * deltaAngleX - deltaZ * self.speed * (1 - deltaAngleX)
        self.lx += deltaX * self.speed * deltaAngleX - deltaZ * self.speed * (1 - deltaAngleX)
        self.y += deltaY * self.speed - deltaZ * self.speed * deltaAngleY 
        self.ly += deltaY * self.speed - deltaZ * self.speed * deltaAngleY 
        self.z += deltaZ * self.speed * deltaAngleX + deltaX * self.speed * (1 - deltaAngleX)
        self.lz += deltaZ * self.speed * deltaAngleX + deltaX * self.speed * (1 - deltaAngleX)

    def lookAt(self, deltaAngleX, deltaAngleY):
        angleX = (abs(self.x - self.lx) / sqrt(pow(self.z - self.lz, 2) + pow(self.x - self.lx, 2)))
        self.lx += sin(angleX + self.speedAngle * deltaAngleX)
        self.lz += -cos(angleX + self.speedAngle * deltaAngleX)
        if deltaAngleX == -1:
            print("left")
        if deltaAngleX == 1:
            print("right")

    def draw(self):
        gluLookAt(self.x, self.y, self.z, self.lx, self.ly, self.lz, 0, 1, 0)

    def update(self, keys_pressed):
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
