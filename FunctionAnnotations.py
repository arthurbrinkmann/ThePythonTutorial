def f(ham: str, eggs: str = 'eggs') -> str:
    print("Annotations:",f.__annotations__)
    print("Arguments:", ham, eggs)
    return ham + ' and ' + eggs


f('spam')
#Output
Annoatations: {'ham': <class 'str'>, 'return': <class 'str', 'eggs': <class 'str'>}
Arguments: spam eggs
'spam and eggs'