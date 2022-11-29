from CircleArray.CircleArray import CircleArray


def test_circle_array():
    assert CircleArray().run(5, 3) == '13524', "Должно быть 13524"
    assert CircleArray().run(4, 3) == '13', "Должно быть 13"
    assert CircleArray().run(0, 0) != '13524', "Должно быть Ошибка"


test_circle_array()
