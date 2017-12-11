from .object import Object, Surface, Edge, Point

def pyramid(x: int = 0) -> Object:
    points = [
        Point(x - 1, x - 1, x - 1, 1),
        Point(x - 1, x - 1, x + 1, 1),
        Point(x + 1, x - 1, x, 1),
        Point(x, x + 1, x, 1)
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
