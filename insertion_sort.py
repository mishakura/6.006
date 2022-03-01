def insertion_sort(arr):
    for i in range(len(arr) - 1):
        j = i
        while j >= 0 and arr[j+1] < arr[j]:
            arr[j+1], arr[j] = arr[j], arr[j+1]
            j -= 1
            

list = [6, 5, 4, 3, 2, 1, 78, 0]
insertion_sort(list)
print(list)


   


           

