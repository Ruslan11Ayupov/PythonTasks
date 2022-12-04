from RectangleArea.Classes.RectangleArea import RectangleArea


def test(actual, expected):
    assert actual == expected, "Ответ: " + str(actual) + ". Должен быть: " + str(expected)


result = RectangleArea(1, 1, 3, 5, 2, 1, 5, 6).run()
test(result, 19)

result = RectangleArea(-3, -2, 0, 3, -1, -1, 1, 2).run()
test(result, 18)

result = RectangleArea(-2, -2, 2, 2, -2, -2, 2, 2).run()
test(result, 16)

result = RectangleArea(-5, -3, 0, 3, -3, -3, 3, 3).run()
test(result, 48)

result = RectangleArea(-5, -3, 0, 5, -3, -3, 3, 3).run()
test(result, 58)

result = RectangleArea(-5, -2, 5, 1, -3, -3, 3, 3).run()
test(result, 48)

result = RectangleArea(-2, -5, 1, 5, -3, -3, 3, 3).run()
test(result, 48)
