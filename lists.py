# All ran in python3.10
squares = [1, 4, 9, 16, 25]
#output 
squares
[1, 4, 9 ,16, 25]
squares[0]
1
squares[-1]
25
squares[-3:]
[9, 16, 25]
squares + [36, 49, 64, 81, 100]
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

cubes = [1, 8, 27, 65, 125]
4 ** 3 
64
cubes[3] = 64
cubes
[1, 8, 27, 64, 125, 216, 343]

cubes.append(216) # add the cube of 6
cubes.append(7**3) # and the cube of 7
cubes
[1, 8, 27, 64, 125, 216, 343]
