def binary_search(arr, object):
    start = 0
    last = len(arr)

    while start < last:
        middle_point = (last + start) // 2
        
        if object == arr[middle_point]:
            return print(f"Object is on Index {middle_point}")
        elif object > arr[middle_point]:
            start = middle_point + 1
        elif object < arr[middle_point]:
            last = middle_point - 1

    return print("Not found")

def binary_recursive(arr, start, last, object):
    middle_point = (last + start) // 2
    if start > last:
        return print("Not Found")
    if object == arr[middle_point]:
        return print(f"Object is on Index {middle_point}")
    elif object > arr[middle_point]:
        binary_recursive(arr, middle_point + 1, last, object)
    elif object < arr[middle_point]:
        binary_recursive(arr, start, middle_point - 1, object)

