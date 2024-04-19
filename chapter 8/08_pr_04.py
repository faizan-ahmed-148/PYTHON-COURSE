# n! = (n-1)! * n 
# sum(n) = sum(n-1) + n

def factorial_recursive(n):
    if n == 1 or n == 0:
        return 1
    return n + factorial_recursive(n-1)
f = factorial_recursive(9)
print(f)

    