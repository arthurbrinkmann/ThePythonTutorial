combs1 = [(x,y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y]
print(combs1)
# is equal to 

combs2 = []
for x in [1, 2, 3]:
    for y in [3, 1, 4]:
        if x != y:
            combs2.append((x,y))
print (combs2) 

