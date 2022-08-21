def linear_search(A, key):
    index = 0
    while index < len(A):
        if key == A[index]:
            return index
        index += 1
    
    return -1

A = [84, 21, 47, 96, 15]
found = linear_search(A, 10)
print(f'Result: {found}')