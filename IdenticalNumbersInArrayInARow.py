LengthArray = int(input())
max = 0
current = 1
number: int
previousNumber: int

for i in range(LengthArray):
    number = int(input())
    if i != 0 and number == previousNumber:
        current += 1
    else:
        current = 1
    if current > max:
        max = current
    previousNumber = number
print(max)