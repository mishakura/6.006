def selection_sort(arr):
    for i in range(len(arr),0, -1):

        if i == len(arr):
            counter = len(arr)
            num = 0
        else:
            var1 = arr[counter - 1]
            arr[counter - 1] = arr[index]
            arr[index] = var1
            index = 0
            counter -= 1   
            num = 0  

        for j in range(counter):
            if arr[j] >= num:
                num = arr[j]
                index = j
    return arr            


def selection_recursive(arr,len):
    num = 0
    index = 0
    if len == 1:
        return arr
    else:
        for i in range(len):
            if arr[i] >= num:
                num = arr[i]
                index = i
        var1 = arr[len - 1]
        arr[len-1] = num
        arr[index] = var1
    selection_recursive(arr,len -1)       
                  
            

listsuru = [5,4,3,2,1,-1,0,245,11,11]
selection_recursive(listsuru, len(listsuru))
print(listsuru)





def prefix_max(A, i):
    if i > 0:
        j = prefix_max(A, i-1)
        if A[i] < A[j]:
            return j
    return i

# [1,2,3,4]
#            