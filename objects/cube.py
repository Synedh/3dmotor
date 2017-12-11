from object import Object, Surface, Edge, Point

def cube(x: int = 0) -> Object:

    points = [
        Point(x + 1, x - 1, x - 1, 1),
        Point(x + 1, x + 1, x - 1, 1),
        Point(x - 1, x + 1, x - 1, 1),
        Point(x - 1, x - 1, x - 1, 1),
        Point(x + 1, x - 1, x + 1, 1),
        Point(x + 1, x + 1, x + 1, 1),
        Point(x - 1, x - 1, x + 1, 1),
        Point(x - 1, x + 1, x + 1, 1)
    ]
    points = [
        Point(-1, -1, -1, 1),
        Point(-1, -1, 1, 1),
        Point(1, -1, 0, 1),
        Point(0, 1, 0, 1)
    ]

    edges = [
        Edge(points[0],points[1], 1),
        Edge(points[0],points[2], 1),
        Edge(points[0],points[3], 1),
        Edge(points[1],points[2], 1),
        Edge(points[1],points[3], 1),
        Edge(points[2],points[3], 1)
    ]

    surfaces = [
        Surface(edges[0], edges[1], edges[3]),
        Surface(edges[3], edges[5], edges[4]),
        Surface(edges[0], edges[4], edges[2]),
        Surface(edges[1], edges[2], edges[5])
    ]

    return Object(points, edges, surfaces)


colors = [
    (0,1,0),
    (1,0.5,0),
    (1,0,0),
    (1,1,0),
    (0,0,1),
    (1,0,1)
]

edges = [
    (0,1),
    (0,3),
    (0,4),
    (2,1),
    (2,3),
    (2,7),
    (6,3),
    (6,4),
    (6,7),
    (5,1),
    (5,4),
    (5,7)
]

surfaces = [
    (0,1,2,3),
    (3,2,7,6),
    (6,7,5,4),
    (4,5,1,0),
    (1,5,7,2),
    (4,0,3,6)
]

def cube() -> Object:
    # Surfaces
    glBegin(GL_QUADS)
    for i, surface in enumerate(surfaces):
        for vertex in surface:
            glColor3fv(colors[i])
            glVertex3fv(verticies[vertex])
    glEnd()

    # Line
    glLineWidth(2)
    glColor3f(1,1,1)
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(verticies[vertex])
    glEnd()

    # Points
    glPointSize(10)
    glColor3f(1,1,1)
    glBegin(GL_POINTS)
    for verticie in verticies:
        glVertex3f(verticie[0], verticie[1], verticie[2])
    glEnd()