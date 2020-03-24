def fib(n):
    '''Returns the nth Fibonacci number'''
    x = 0
    y = 1
    i = 0
    for _ in range(n):
        x = y
        y = i
        i = x + y
    return i
