from points import Point


class Rectangle:
    #Lewy dolny punkt - pt1, prawy górny - pt2

    def __init__(self, pt1, pt2):
        if not isinstance(pt1, Point) or not isinstance(pt2, Point):
            raise TypeError("rectangle potrzebuje dwoch punktow")

        if pt1.x >= pt2.x or pt1.y >= pt2.y:
            raise ValueError("punkty musza byc: lewy_dolny, prawy_gorny")

        self.pt1 = pt1
        self.pt2 = pt2

    @classmethod
    def from_points(cls, points):
        if len(points) != 2:
            raise ValueError("from_points wymaga dokladnie dwoch punktow")
        return cls(points[0], points[1])

    @property
    def left(self):
        return self.pt1.x

    @property
    def right(self):
        return self.pt2.x

    @property
    def bottom(self):
        return self.pt1.y

    @property
    def top(self):
        return self.pt2.y

    @property
    def width(self):
        return self.right - self.left

    @property
    def height(self):
        return self.top - self.bottom


    @property
    def topleft(self):
        return Point(self.left, self.top)

    @property
    def bottomleft(self):
        return Point(self.left, self.bottom)


    @property
    def topright(self):
        return Point(self.right, self.top)

    @property
    def bottomright(self):
        return Point(self.right, self.bottom)

    @property
    def center(self):

        return Point(
            (self.left + self.right) / 2,
            (self.bottom + self.top) /2
        )

    def __str__(self):
        return f"Rectangle({self.pt1}, {self.pt2})"

    def __repr__(self):
        return f"Rectangle({self.pt1!r}, {self.pt2!r})"

    def __eq__(self, other):
        return self.pt1 == other.pt1 and self.pt2 == other.pt2