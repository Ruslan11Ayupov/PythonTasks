from RectangleArea.Classes.Point import Point

from RectangleArea.Classes.Rectangle import Rectangle

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

    def run(self) -> int:
        result: int = self.summedAreaOfTwoRectangles()

        pointsInA: list[Point] = self.rectangleA.containsPoints(self.rectangleB)
        pointsInB: list[Point] = self.rectangleB.containsPoints(self.rectangleA)

        amountPoints: int = self.amountOfPointsInOneOfRectangles(pointsInA, pointsInB)

        pointsA: list[Point] = self.rectangleA.getPoints()
        pointsB: list[Point] = self.rectangleB.getPoints()

        if amountPoints == 0:
            result -= self.amountPointsZero(pointsA, pointsB)

        elif amountPoints == 1:
            result -= self.amountPointsOne(pointsInA, pointsInB)

        elif amountPoints == 2:
            result -= self.amountPointsTwo(pointsInA, pointsInB)

        elif amountPoints == 4:
            result -= self.amountPointsFour(pointsInA, pointsInB)

        return result

    def amountOfPointsInOneOfRectangles(self, pointsInA: list[Point], pointsInB: list[Point]) -> int:
        return len(pointsInB) if len(pointsInB) > len(pointsInA) else len(pointsInA)

    def amountPointsZero(self, pointsA, pointsB) -> int:
        listPoints: list = []
        for i in range(0, len(pointsA)):
            linePointA1 = pointsA[i]
            if i == len(pointsA) - 1:
                linePointA2 = pointsA[0]
            else:
                linePointA2 = pointsA[i + 1]
            for j in range(0, len(pointsB)):
                linePointB1 = pointsB[j]
                if j == len(pointsB) - 1:
                    linePointB2 = pointsB[0]
                else:
                    linePointB2 = pointsB[j + 1]
                if (linePointB1.y < linePointA1.y < linePointB2.y or linePointB1.y > linePointA1.y > linePointB2.y) \
                        and (
                        linePointA1.x < linePointB1.x < linePointA2.x or linePointA1.x > linePointB1.x > linePointA2.x):
                    listPoints.append(Point(linePointB1.x, linePointA1.y))
                elif (linePointA1.y < linePointB1.y < linePointA2.y or linePointA1.y > linePointB1.y > linePointA2.y) \
                        and (
                        linePointB1.x < linePointA1.x < linePointB2.x or linePointB1.x > linePointA1.x > linePointB2.x):
                    listPoints.append(Point(linePointA1.x, linePointB1.y))
        if len(listPoints) > 2:
            point2: Point = listPoints[1]
            point3: Point = listPoints[2]
            return abs(point2.x - point3.x) * abs(point2.y - point3.y)

    def amountPointsOne(self, pointsInA: list[Point], pointsInB: list[Point]) -> int:
        pointA: Point = pointsInB[0]
        pointB: Point = pointsInA[0]
        return abs(pointA.x - pointB.x) * abs(pointA.y - pointB.y)

    def amountPointsTwo(self, pointsInA: list[Point], pointsInB: list[Point]) -> int:
        if len(pointsInB) == 2:
            pointA1: Point = pointsInB[0]
            pointA2: Point = pointsInB[1]
            if pointA2.x != pointA1.x:
                if pointA1.y < self.rectangleA.xy2.y:
                    return (abs(pointA2.x - pointA1.x)) * (self.rectangleB.xy2.y - pointA1.y)
                elif pointA1.y == self.rectangleA.xy2.y:
                    return (abs(pointA2.x - pointA1.x)) * (pointA2.y - self.rectangleB.xy1.y)
            elif pointA1.y != pointA2.y:
                if pointA1.x < self.rectangleA.xy2.x:
                    return (abs(pointA2.y - pointA1.y)) * (self.rectangleB.xy2.x - pointA1.x)
                elif pointA1.x == self.rectangleA.xy2.x:
                    return (abs(pointA2.y - pointA1.y)) * (pointA2.x - self.rectangleB.xy1.x)
        elif len(pointsInA) == 2:
            pointB1: Point = pointsInA[0]
            pointB2: Point = pointsInA[1]
            if pointB2.x != pointB1.x:
                if pointB1.y < self.rectangleB.xy2.y:
                    return (abs(pointB2.x - pointB1.x)) * (self.rectangleA.xy2.y - pointB1.y)
                elif pointB1.y == self.rectangleB.xy2.y:
                    return (abs(pointB2.x - pointB1.x)) * (pointB2.y - self.rectangleA.xy1.y)
            elif pointB1.y != pointB2.y:
                if pointB1.x < self.rectangleB.xy2.x:
                    return (abs(pointB2.y - pointB1.y)) * (self.rectangleA.xy2.x - pointB1.x)
                elif pointB1.x == self.rectangleB.xy2.x:
                    return (abs(pointB2.y - pointB1.y)) * (pointB2.x - self.rectangleA.xy1.x)

    def amountPointsFour(self, pointsInA: list[Point], pointsInB: list[Point]) -> int:
        if len(pointsInB) == 4:
            return (self.rectangleB.xy2.x - self.rectangleB.xy1.x) * (self.rectangleB.xy2.y - self.rectangleB.xy1.y)
        elif len(pointsInA) == 4:
            return (self.rectangleA.xy2.x - self.rectangleA.xy1.x) * (self.rectangleA.xy2.y - self.rectangleA.xy1.y)

    def summedAreaOfTwoRectangles(self) -> int:
        return ((self.rectangleA.xy2.x - self.rectangleA.xy1.x) * (self.rectangleA.xy2.y - self.rectangleA.xy1.y)) + \
              ((self.rectangleB.xy2.x - self.rectangleB.xy1.x) * (self.rectangleB.xy2.y - self.rectangleB.xy1.y))
