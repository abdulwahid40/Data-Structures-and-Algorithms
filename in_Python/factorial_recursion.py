def factorial_recursion(n):
    if n == 0:
        return 1
    return factorial_recursion(n-1) * n


n = input("Enter number to caluclate factorial: ")
n = int(n)
print(factorial_recursion(n))