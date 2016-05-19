numbersList = []

for n in range(1, 101, 1):
    numbersList.append(n)

print(numbersList)

sum_squares = 0
square_sum = 0

for number in numbersList:
    sum_squares += (number ** 2)
    square_sum += number

square_sum **= 2

print(square_sum-sum_squares)
