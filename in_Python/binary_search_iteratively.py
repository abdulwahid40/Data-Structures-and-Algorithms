def binary_search_iteratively(A, key):
    left_index = 0
    right_index = len(A) - 1

    while left_index <= right_index:
        mid_point = (left_index + right_index) // 2
        print(mid_point)
        if key == A[mid_point]:
            return mid_point
        elif key < A[mid_point]:
            right_index = mid_point - 1
        elif key > A[mid_point]:
            left_index = mid_point + 1
    
    return -1

A = [15, 21, 47, 84, 96]
found = binary_search_iteratively(A, 21)
print(f'Result: {found}')