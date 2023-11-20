def fibonacci_iterative(n):
    if n <= 1:
        return n
    fib_prev, fib_current = 0, 1
    for _ in range(2, n + 1):
        fib_prev, fib_current = fib_current, fib_prev + fib_current
    return fib_current
n = 10
result_iterative = fibonacci_iterative(n)
print(f"Fibonacci Iterative({n}):", result_iterative)