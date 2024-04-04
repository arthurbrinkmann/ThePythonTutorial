def fib(n):
     """Print a Fibonacci series up to n."""
     a, b = 0, 1
     while a < n:
         print(a, end='')
         a, b = b, a+b
     fib(2000)

# Other names can also point to that same function object and can also be used to access the function:
     fib
     f = fib 
     f(2000)

# Writing the value None is normall suppressed by the interpreter if it would be the only value writte. You can see it if you really want to using print():
     fib(0)
     print(fib(0))