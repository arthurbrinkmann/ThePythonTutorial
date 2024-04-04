# All ran in python3.10
word = 'Python'
word[0]
'P'
word[5]
'n'
word[-1]
'n'
word[-2]
'o'
word[-6]
'P'

word[0:2]
'Py'
word[2:5]
'tho'

word[:2]
'Py'
word[4:]
'on'
word[-2:]
'on'

'J' + word [1:]
'Jython'

word[:2] + 'py'
'Pypy'

word[42]  # the word only has 6 characters
#Traceback (most recent call last):
#  File "<stdin>", line 1, in <module>
#IndexError: string index out of range

s = 'supercalifragilisticexpialidocious'
len(s)
#34