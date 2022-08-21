def sum_nautral_numbers_recursion(n):
    if n == 0:
        return n
    return sum_nautral_numbers_recursion(n-1) + n

n = input("Enter number for summ of n natural numbers: ")
n = int(n)
print(sum_nautral_numbers_recursion(n))
