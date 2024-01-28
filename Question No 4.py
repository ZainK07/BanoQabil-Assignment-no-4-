# Write a Python program to print the Fibonacci series.

def fibonacci(n):
    fib_series = [0, 1]

    while len(fib_series) < n:
        fib_series.append(fib_series[-1] + fib_series[-2])

    return fib_series


num_terms = 10
result = fibonacci(num_terms)

print(f"Fibonacci series up to {num_terms} terms: {result}")
