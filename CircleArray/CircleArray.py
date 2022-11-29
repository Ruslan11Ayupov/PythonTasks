class CircleArray:

    def run(self, n, m):
        result: str = ''
        pointer = 0
        nFormated = []

        for i in range(1, n + 1):
            nFormated.append(i)

        while True:
            result += str(nFormated[pointer])
            pointer += (m - 1)
            if pointer >= n:
                pointer -= n
                if pointer == 0:
                    break
        return result


"""
Круговой массив - массив из элементов, в котором по достижению конца массива следующим элементом будет снова первый. Mассив задается числом n, то есть представляет собой числа от 1 до n.
Пример кругового массива для n=3:

Напишите программу, которая выводит путь, по которому, двигаясь интервалом длины m по заданному массиву, концом будет являться первый элемент.
Началом одного интервала является конец предыдущего. Путь - массив из начальных элементов полученных интервалов.
Пример 1:
n = 4, m = 3 Решение:
Круговой массив: 1234. При длине обхода 3 получаем интервалы: 123, 341. Полученный путь: 13.
Пример 2:
n = 5, m = 4 Решение:
Круговой массив: 123456. При длине обхода 4 получаем интервалы: 1234, 4512, 2345, 5123, 3451. Полученный путь: 14253.
Параметры передаются в качестве аргументов командной строки.
Например, для последнего примера на вход подаются аргументы: 5 4
Ожидаемый вывод в консоль: 14253
"""