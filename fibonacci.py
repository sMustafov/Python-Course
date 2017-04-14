def fib(n):
    first, second = 0, 1
    while first <= n:
        print(first, end=' ')
        first, second = second, second + first