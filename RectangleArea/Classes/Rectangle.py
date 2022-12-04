from RectangleArea.Classes.Point import Point

class Rectangle:
    xy1: Point
    xy2: Point
    xy3: Point
    xy4: Point

    def __init__(self, xy1: Point, xy2: Point, xy3: Point, xy4: Point):
        self.xy1 = xy1
        self.xy2 = xy2
        self.xy3 = xy3
        self.xy4 = xy4

    def containsPoint(self, point: Point) -> bool:
        return self.xy2.x >= point.x >= self.xy1.x and self.xy2.y >= point.y >= self.xy1.y

    def getPoints(self) -> list[Point]:
        return [self.xy1, self.xy3, self.xy2, self.xy4]

    def containsPoints(self, rectangleSecond) -> list[Point]:
        points = list()
        if self.containsPoint(rectangleSecond.xy1):
            points.append(rectangleSecond.xy1)
        if self.containsPoint(rectangleSecond.xy2):
            points.append(rectangleSecond.xy2)
        if self.containsPoint(rectangleSecond.xy3):
            points.append(rectangleSecond.xy3)
        if self.containsPoint(rectangleSecond.xy4):
            points.append(rectangleSecond.xy4)
        return points
