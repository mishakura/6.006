
def radix(A, digits):
    for i in range(len(digits)):
        bucket = [[] for i in range(10)]
        for item in A:
            index = item // 10 ** (i) % 10
            bucket[index].append(item)
        A = [item for sublist in bucket for item in sublist]
    return A


A = [55,45,3,289,213,1,288,53,2]
maxDigitNum = (str(max(A)))
A = radix(A, maxDigitNum)
print(A)
