def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


print(fibonacci(3))


def fibonacci_loop(n):
    if n == 1 or n == 2:
        return 1
    else:
        fib1 = 1
        fib2 = 1
        fib3 = 0
        for i in range(2, n):
            fib3 = fib1 + fib2
            fib1 = fib2
            fib2 = fib3
        return fib3


print(fibonacci_loop(3))
