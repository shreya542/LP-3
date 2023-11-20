def fibonacci_recursive(n):
    if n <= 1:
        return n
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)
n = 10
result_recursive = fibonacci_recursive(n)
print(f"Fibonacci Recursive({n}):", result_recursive)