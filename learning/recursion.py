def fact(n):
    if n >= 1:
        return n*fact(n-1)
    else:
        return 1

print(fact(2)) # 2
print(fact(4)) # 24

def fib(n):

    if n > 1:
        return (fib(n-1) + fib(n-2))
    elif n == 1:
        return 1
    else:
        return 0

print(fib(10)) # 55



