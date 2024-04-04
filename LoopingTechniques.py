# When looping through dictionaries, the key and corresponding value can be retrieved at the same time using the items() method
knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items():
    print(k, v)

# When looping through a sequence the position index and corresponding value can be retrieved at the same time using the enumerate() function

for i, v in enumerate(['tic', 'tac', 'toe']):
    print(i, v)

# To loop over two or more quences at the same time, the entries can be paired with the zip() function
questoins = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questoins, answers):
    print('What is your{0}? It is {1}.' .format(q, a))

    
