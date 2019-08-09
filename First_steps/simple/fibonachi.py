def fibonachi(count):
    a, b = 0, 1
    for _ in range(count):
        yield b
        a, b = b, a + b



f = fibonachi(5)
next(f)
next(f)
next(f)

count = int(input('how many fibonachi numbers to print? '))
for i in fibonachi(count):
    print(i)

"""
рекурсия:
fib = lambda n: fib(n - 1) + fib(n - 2) if n > 2 else 1
или
def fibonacci(n):
    if n in (1, 2):
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)
 
 
print(fibonacci(10))


цикл:

"""
