def factorial(n):
    if n == 1: return 1
    return n * factorial(n-1)

print(factorial(3))
print(factorial(5))
print(factorial(9))
print(factorial(15))
print(factorial(20))