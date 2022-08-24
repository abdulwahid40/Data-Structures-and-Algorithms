def bubble_sort(A):
    n = len(A)
    for passes in range(n-1, 0, -1):
        for i in range(passes):
            if A[i] > A[i+1]:
                temp = A[i]
                A[i] = A[i+1]
                A[i+1] = temp


A = [3, 5, 8, 9, 6, 2]
print(f"Original Array: {A}")
bubble_sort(A)
print(f"Sorted Array: {A}")