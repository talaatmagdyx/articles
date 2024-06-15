values = [1, 2, 3, 4, 5]
squares = []
for x in values:
    if (y := x * x) > 10:
        squares.append(y)
print(squares)