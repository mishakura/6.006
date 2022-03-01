def countSort(array, k):
    kArray = [0 for i in range(k)]
    
    for number in array:
        kArray[number] += 1
    
    for i in range(1, len(kArray)):
        sum = kArray[i - 1]
        kArray[i] += sum
    sorted_array = [0 for i in range(len(array))]
    for i in range(len(array) - 1, -1, -1):
        value = array[i]
        index = kArray[value]
        sorted_array[index - 1] = value
        kArray[value] -= 1
    return sorted_array

array = [1,4,1,2,7,5,2]
k = 10
print(countSort(array, k))