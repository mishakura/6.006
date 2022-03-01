def count_long_subarray(A):
    '''
    Input:  A     | Python Tuple of positive integers
    Output: count | number of longest increasing subarrays of A
    '''
    count = 0
    increasing_subarray = []
    i = 0
    max = 0
    while i < len(A) - 1:
        leng = 0
        var = 0
        while A[i] > var:
            leng += 1
            var = A[i]
            i += 1
            if i > len(A)- 1:
                break
        if leng > 1:
            increasing_subarray.append(leng)
        if leng > max:
            max = leng
        
    if len(increasing_subarray) == 0:
        return None
    for i in range(len(increasing_subarray)):
        
        if increasing_subarray[i] >= max:
            count += 1
    return count

