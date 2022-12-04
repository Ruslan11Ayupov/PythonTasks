class Point:
    x: int
    y: int

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y


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


class RectangleArea:
    rectangleA: Rectangle
    rectangleB: Rectangle

    def __init__(self, ax1, ay1, ax2, ay2, bx1, by1, bx2, by2):
        a1 = Point(ax1, ay1)
        a2 = Point(ax2, ay2)
        a3 = Point(ax1, ay2)
        a4 = Point(ax2, ay1)
        b1 = Point(bx1, by1)
        b2 = Point(bx2, by2)
        b3 = Point(bx1, by2)
        b4 = Point(bx2, by1)
        self.rectangleA = Rectangle(a1, a2, a3, a4)
        self.rectangleB = Rectangle(b1, b2, b3, b4)

    def containsPoints(self, rectangleFirst: Rectangle, rectangleSecond: Rectangle) -> list:
        points = list()
        if rectangleFirst.containsPoint(rectangleSecond.xy1):
            points.append(rectangleSecond.xy1)
        if rectangleFirst.containsPoint(rectangleSecond.xy2):
            points.append(rectangleSecond.xy2)
        if rectangleFirst.containsPoint(rectangleSecond.xy3):
            points.append(rectangleSecond.xy3)
        if rectangleFirst.containsPoint(rectangleSecond.xy4):
            points.append(rectangleSecond.xy4)
        return points

    def run(self):
        pointsInA = self.containsPoints(self.rectangleA, self.rectangleB)
        pointsInB = self.containsPoints(self.rectangleB, self.rectangleA)

        amountPoints = len(pointsInB) if len(pointsInB) > len(pointsInA) else len(pointsInA)

        result = ((self.rectangleA.xy2.x - self.rectangleA.xy1.x) * (self.rectangleA.xy2.y - self.rectangleA.xy1.y)) + \
                 ((self.rectangleB.xy2.x - self.rectangleB.xy1.x) * (self.rectangleB.xy2.y - self.rectangleB.xy1.y))
        pointsA = self.rectangleA.getPoints()
        pointsB = self.rectangleB.getPoints()
        if amountPoints == 0:
            listPoints: list = []
            for i in range(0, len(pointsA)):
                linePointA1 = pointsA[i]
                if i == len(pointsA) - 1:
                    linePointA2 = pointsA[0]
                else:
                    linePointA2 = pointsA[i+1]
                for j in range(0, len(pointsB)):
                    linePointB1 = pointsB[j]
                    if j == len(pointsB) - 1:
                        linePointB2 = pointsB[0]
                    else:
                        linePointB2 = pointsB[j + 1]
                    if (linePointB1.y < linePointA1.y < linePointB2.y or linePointB1.y > linePointA1.y > linePointB2.y) \
                            and (linePointA1.x < linePointB1.x < linePointA2.x or linePointA1.x > linePointB1.x > linePointA2.x):
                        listPoints.append(Point(linePointB1.x, linePointA1.y))
                    elif (linePointA1.y < linePointB1.y < linePointA2.y or linePointA1.y > linePointB1.y > linePointA2.y) \
                            and (linePointB1.x < linePointA1.x < linePointB2.x or linePointB1.x > linePointA1.x > linePointB2.x):
                        listPoints.append(Point(linePointA1.x, linePointB1.y))
            if len(listPoints) > 2:
                point2: Point = listPoints[1]
                point3: Point = listPoints[2]
                result -= abs(point2.x - point3.x) * abs(point2.y - point3.y)
        elif amountPoints == 1:
            pointA: Point = pointsInB[0]
            pointB: Point = pointsInA[0]
            result -= abs(pointA.x - pointB.x) * abs(pointA.y - pointB.y)
        elif amountPoints == 2:
            if len(pointsInB) == 2:
                pointA1: Point = pointsInB[0]
                pointA2: Point = pointsInB[1]
                if pointA2.x != pointA1.x:
                    if pointA1.y < self.rectangleA.xy2.y:
                        result -= (abs(pointA2.x - pointA1.x)) * (self.rectangleB.xy2.y - pointA1.y)
                    elif pointA1.y == self.rectangleA.xy2.y:
                        result -= (abs(pointA2.x - pointA1.x)) * (pointA2.y - self.rectangleB.xy1.y)
                elif pointA1.y != pointA2.y:
                    if pointA1.x < self.rectangleA.xy2.x:
                        result -= (abs(pointA2.y - pointA1.y)) * (self.rectangleB.xy2.x - pointA1.x)
                    elif pointA1.x == self.rectangleA.xy2.x:
                        result -= (abs(pointA2.y - pointA1.y)) * (pointA2.x - self.rectangleB.xy1.x)
            elif len(pointsInA) == 2:
                pointB1: Point = pointsInA[0]
                pointB2: Point = pointsInA[1]
                if pointB2.x != pointB1.x:
                    if pointB1.y < self.rectangleB.xy2.y:
                        result -= (abs(pointB2.x - pointB1.x)) * (self.rectangleA.xy2.y - pointB1.y)
                    elif pointB1.y == self.rectangleB.xy2.y:
                        result -= (abs(pointB2.x - pointB1.x)) * (pointB2.y - self.rectangleA.xy1.y)
                elif pointB1.y != pointB2.y:
                    if pointB1.x < self.rectangleB.xy2.x:
                        result -= (abs(pointB2.y - pointB1.y)) * (self.rectangleA.xy2.x - pointB1.x)
                    elif pointB1.x == self.rectangleB.xy2.x:
                        result -= (abs(pointB2.y - pointB1.y)) * (pointB2.x - self.rectangleA.xy1.x)
        elif amountPoints == 4:
            if len(pointsInB) == 4:
                result = ((self.rectangleB.xy2.x - self.rectangleB.xy1.x) * (self.rectangleB.xy2.y - self.rectangleB.xy1.y))
            elif len(pointsInA) == 4:
                result = ((self.rectangleA.xy2.x - self.rectangleA.xy1.x) * (self.rectangleA.xy2.y - self.rectangleA.xy1.y))
        return result
