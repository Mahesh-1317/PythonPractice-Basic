def fib(n):
    if n <= 0:
        return
    elif n == 1 or n == 2:
        return 1
    else:
        fibo1 = fib(n-1)
        fibo2 = fib(n-2)
        fibo = fibo1 + fibo2
        return fibo
print(fib(5))