def selection_sort(A):
    j = 0
    index = 0

    for i in range(j, len(A) - 1):
        min = A[j]
        for k in range(j, len(A) - 1):
            if A[k + 1] < A[k]:
                index = k + 1
                min = A[k + 1]
        A[j] , A[index] = A[index] , A[j]
        j += 1

list = [64,25,12,22,11]
selection_sort(list)
print(list)            