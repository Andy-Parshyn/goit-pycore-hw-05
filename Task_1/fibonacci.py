

def caching_fibonacci():
    cache = dict()

    def  fibonacci(n: int):
        if n in cache:
            return cache[n]
        
        if n < 2 :
            return n
        else:
            cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
            return cache[n]
        
    return fibonacci

fib = caching_fibonacci()

print(fib(10))
print(fib(15))
print(fib(0))
print(fib(1))

