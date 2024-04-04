squares = []
for x in range(10):
    squares.append(x**2)
    print(squares)

    # Could run this 
    squares = list(map(lambda x: x**2, range(10)))
    # Or 
    squares = [x**2 for x in range(10)]