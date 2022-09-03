def radixsort(A):
    n = len(A)
    maxelement = max(A)
    digits = len(str(maxelement))
    l = []
    bins = [l] * 10

    for i in range(digits):
        for j in range(n):
            e = int((A[j] / (10 ** i)) % 10)
            if len(bins[e]) > 0:
                bins[e].append(A[j])
            else:
                bins[e] = [A[j]]

        c = 0
        for a in range(10):
            if len(bins[a]) > 0:
                for b in range(len(bins[a])):
                    A[c] = bins[a].pop(0)
                    c += 1 


A = [63, 250, 835, 947, 651, 28]
print(f"Original Array: {A}")
radixsort(A)
print(f"Sorted Array: {A}")


