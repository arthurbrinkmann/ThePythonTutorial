matrix = [
    [ 1, 2, 3, 4],
    [5, 6, 7, 8], 
    [9, 10, 11, 12],
]

# Following list comprehnesion will transpose rows and columns
transposed1= [[row[i] for row in matrix] for i in range(4)]
print(transposed1)

# Same as above
transposed2 = []
for i in range (4):
    transposed2.append([row[i] for row in matrix])

    print(transposed2)