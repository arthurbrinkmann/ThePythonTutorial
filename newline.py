s = 'First line.\nSecond line.'  # \n means newline
s  # without print(), special characters are included in the string
'First line.\nSecond line.'
print(s)  # with print(), special characters are interpreted, so \n produces new line

print('C:\some\name')  # here \n means newline!

print(r'C:\some\name')  # note the r before the quote
