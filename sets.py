basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)
print('orange' in basket)
print('crabgrass' in basket)
a = set('abracadabra')
b = set('alacazam')
print(a) # unique letters in a 
print(a-b) # Letters in a but not in b 
print(a | b) # Letters in a or b or both
print(a & b) # Letters in both a and b 
print(a ^ b) # Letters in a or b but not both

# Similarly to list comprehensions, set comprehensions are also supported:
a = { x for x in 'abracadabra' if x not in 'abc'}
print(a)