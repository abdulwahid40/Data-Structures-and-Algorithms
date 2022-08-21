
def binary_search_recursion(A, key, left_index, right_index):
    if left_index > right_index:
        return -1
    else:
        mid_point = (left_index + right_index) // 2
        if key == A[mid_point]:
            return mid_point
        elif key < A[mid_point]:
            return binary_search_recursion(A, key, left_index, mid_point - 1)
        elif key > A[mid_point]:
            return binary_search_recursion(A, key, mid_point + 1, right_index)


A = [15, 21, 47, 84, 96]
found = binary_search_recursion(A, 84, 0, len(A))
print(f'Result: {found}')




