import pytest
from Rectangle import Rectangle
from points import Point


def test_from_points():
    p1 = Point(1, 2)
    p2 = Point(4, 6)

    r = Rectangle.from_points((p1, p2))
    assert r.pt1 == p1
    assert r.pt2 == p2


def test_properties_coordinates():
    r = Rectangle(Point(1, 2), Point(4, 6))

    assert r.left == 1
    assert r.right == 4
    assert r.bottom == 2
    assert r.top == 6
    assert r.width == 3
    assert r.height == 4


def test_corner_points():
    r = Rectangle(Point(1, 2), Point(4, 6))

    assert r.topleft == Point(1, 6)
    assert r.topright == Point(4, 6)
    assert r.bottomleft == Point(1, 2)
    assert r.bottomright == Point(4, 2)


def test_center():
    r = Rectangle(Point(0, 0), Point(4, 4))
    assert r.center == Point(2, 2)

def test_invalid_points():
    with pytest.raises(ValueError):
        Rectangle(Point(3, 3), Point(1, 1))