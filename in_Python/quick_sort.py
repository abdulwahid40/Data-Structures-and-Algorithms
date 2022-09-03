def quicksort(A, low, high):
    if low < high:
        pi = partition(A, low, high)    # returns the index of pivot element or partition element
        quicksort(A, low, pi-1)
        quicksort(A, pi+1, high)


def partition(A, low, high):
    pivot = A[low]
    i = low + 1
    j = high

    while True:
        while i <= j and A[i] <= pivot:
            i += 1
        while i <= j and A[j] > pivot:
            j -= 1

        if i <= j:
            A[i], A[j] = A[j], A[i]
        else:
            break

    A[low], A[j] = A[j], A[low]
    return j


A = [3, 5, 8, 9, 6, 2]
print(f"Original Array: {A}")
quicksort(A, 0, len(A)-1)
print(f"Sorted Array: {A}")
