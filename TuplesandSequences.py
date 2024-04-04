t = 12345, 54321, 'hello'
t [0]
print(t)

# Tuples may be nested
u = t, (1, 2, 3, 4, 5)
print(u)

# t[0] = 88888
# error occurs stating "'tuple' object does not support item assigment"

# They can contain mutable objects:
v = ([1, 2, 3], [3, 2, 1])
v[0][0]=10
print(v)