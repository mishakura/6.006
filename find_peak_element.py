import random

def findPeakElement(arr):
    left = 0
    right = len(arr) - 1
    
    while left < right:
        mid = (left+right) // 2
        if arr[mid] > arr[mid+1]:
            right = mid
        else:
            left = mid + 1
    return left      



list = [random.randint(0,50) for i in range(10)]
print(list)
print(list[findPeakElement(list)])










   
        
