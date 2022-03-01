def heapify(A, i, n):
    #Base case 1
    if i == - 1:
        return
    
    # We reach leaves

    #Checking for left child
    if (2 * i )+ 1 > len(A) - 1:   
        return
    
    child = (2* i) + 1 
   
    #Checking for right child
    if (2 * i )+ 2 <= len(A) - 1:

        if A[(2* i) + 2] > A[child]:
            child = (2* i) + 2
            
    if child >= n:
        return        
    elif A[child] > A[i]: 
        A[child], A[i] = A[i] , A[child]
        return heapify(A, child, n)

def build_heap(A):
    for i in range((len(A) - 1) // 2 , -1, - 1):
        heapify(A, i, len(A) + 1)

    del_last_item = len(A) - 1
    for i in range(len(A) - 1):
        A[0] , A[del_last_item] = A[del_last_item], A[0]
        heapify(A, 0, del_last_item)
        del_last_item -= 1    




    


list = [18,50,39,1,3,19,100]
build_heap(list)
print(list)


   

