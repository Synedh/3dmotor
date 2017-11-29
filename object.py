import random
from OpenGL.GL import *

class Point:
    def __init__(self, x: (int, int, int), y: (int, int, int), z: (int, int, int), mass: float):
        self.x = x
        self.y = y
        self.z = z
        self.mass = mass

    def coords(self) -> [int]:
        return [self.x, self.y, self.z]

class Edge:
    def __init__(self, pointA: Point, pointB: Point, elasticity: float):
        self.pointA = pointA
        self.pointB = pointB
        self.elasticity = elasticity

    def coords(self) -> [[int]]:
        return [self.pointA.coords(), self.pointB.coords()]


class Surface:
    def __init__(self, edgeA: Edge, edgeB: Edge, edgeC: Edge):
        self.edgeA = edgeA
        self.edgeB = edgeB
        self.edgeC = edgeC

    def coords(self) -> [[int]]:
        points = [self.edgeA.pointA.coords()]
        points.append(self.edgeB.pointA.coords() if self.edgeB.pointA.coords() not in points else self.edgeB.pointB.coords())
        points.append(self.edgeC.pointA.coords() if self.edgeC.pointA.coords() not in points else self.edgeC.pointB.coords())
        return points


class Object:
    def __init__(self, points: [Point], edges: [Edge], surfaces: [Surface]):
        self.points = points
        self.edges = edges
        self.surfaces = surfaces

    def update(self):
        # Gravity
        # Speed
        pass

    def draw(self):
        # Surfaces
        glBegin(GL_TRIANGLES)
        for surface in self.surfaces:
            glColor3f(1, 0.5, 0)
            glVertex3fv(surface.coords()[0])
            glVertex3fv(surface.coords()[1])
            glVertex3fv(surface.coords()[2])
        glEnd()

        # Edges
        glLineWidth(2)
        glColor3f(1,1,1)
        glBegin(GL_LINES)
        for edge in self.edges:
            glVertex3fv(edge.coords()[0])
            glVertex3fv(edge.coords()[1])
        glEnd()

        # Points
        glPointSize(10)
        glColor3f(1,1,1)
        glBegin(GL_POINTS)
        for point in self.points:
            glVertex3fv(point.coords())
        glEnd()
