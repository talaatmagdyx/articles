values = [1, 2, 3, 4, 5]
squares = [y for x in values if (y := x * x) > 10]
print(squares)