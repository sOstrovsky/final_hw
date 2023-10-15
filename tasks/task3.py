def fibonacci_cache(func):
    cache = {}

    def cache_wrapper(n):
        if n not in cache:
            cache[n] = func(n)
        return cache[n]

    return cache_wrapper


@fibonacci_cache
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


def print_result():
    print(fibonacci(5))
    print(fibonacci(6))
    print(fibonacci(7))
    print(fibonacci(8))
    print(fibonacci(5))
