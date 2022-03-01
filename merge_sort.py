def mergeArr(arr1,arr2):
    merged_arr = []
    i = 0
    j = 0
    k = 0
    while k < len(arr1) + len(arr2):
        if arr1[i] < arr2[j]:
            merged_arr.append(arr1[i])
            i += 1
            k += 1
        elif arr1[i] > arr2[j]:
            merged_arr.append(arr2[j])
            j += 1
            k += 1
        if i == len(arr1):
            while j != len(arr2):
                merged_arr.append(arr2[j])
                j += 1
                k += 1
        if j == len(arr2):
            while i != len(arr1):
                merged_arr.append(arr1[i])
                i += 1
                k += 1
    return merged_arr   

def mergeSort(arr):
    if len(arr) == 1:
        return arr
    left = arr[:len(arr)//2]
    right = arr[len(arr)//2:]

    a = mergeSort(left)
    b = mergeSort(right)

    return mergeArr(a, b)


list = [6,10,1,5,0,100,99,800,3]  

print(mergeSort(list))