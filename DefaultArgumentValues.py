def ask_ok(prompt, retries=4, reminder='Please try again!'):
    while True:
        reply = input(prompt)
        if reply in {'y', 'ye', 'yes'}:
            return True
        if reply in {'n', 'no', 'nop', 'nope'}:
            return False
        retries = retries - 1 
        if retries < 0: 
            raise ValueError('invalud user response')
        print(reminder)

# Added this for an output on my own
result = ask_ok('Do you want to contuine? (y/n): ')
print('User response: ', result)