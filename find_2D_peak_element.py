import random

def find_max_global(arr, mid_j):
    max_global = 0
    index = 0
    for i in range(len(arr)):
        if arr[i][mid_j] >= max_global:     
            max_global = arr[i][mid_j]
            index = i
    return index 


def find2DPeak(arr,l,r):
    if l == r:
        mid_j = (l + r) // 2       
        return arr[find_max_global(arr,mid_j)][mid_j]
        
    # Pick middle column j = m/2
    mid_j = (l + r) // 2
    # Find global max in mid_j
    max_global = find_max_global(arr, mid_j)

    
    # Compare (i, j − 1),(i, j),(i, j + 1)
    #if mid_j >= 1 and mid_j < len(arr[0]) - 1:
    #if arr[max_global][mid_j] > arr[max_global][mid_j+ 1]:
    #   return arr[max_global][mid_j]
    if arr[max_global][mid_j] > arr[max_global][mid_j + 1]:
        return find2DPeak(arr, l, mid_j)
    else:
        return find2DPeak(arr, mid_j + 1, r)
        
    #else:
    #    if mid_j == 0:
    #        if arr[max_global][mid_j] > arr[max_global][mid_j + 1]:
    #            return arr[max_global][mid_j]
     #       elif arr[max_global][mid_j] < arr[max_global][mid_j + 1]:
    #               return find2DPeak(arr, mid_j + 1, r)
     #   if mid_j == len(arr[0]) - 1:
   #         if arr[max_global][mid_j] > arr[max_global][mid_j - 1]:
   #             return arr[max_global][mid_j]
    #        elif arr[max_global][mid_j] < arr[max_global][mid_j - 1]:
   #             return find2DPeak(arr, l, mid_j - 1)   


        


list = [[random.randint(0,50) for i in range(4)]for i in range (4)]
for i in range(len(list)):
    print(list[i])
print(find2DPeak(list, 0,len(list[1])-1))



           
        

    