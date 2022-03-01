# Uses python3
import sys

def optimal_summands(n):
    #write your code here
    summands = []
    total = n
    index = 1
    test_next_number = n
    if n == 1:
        summands.append(1)
        return summands
    if n == 2:
        summands.append(2)
        return summands

    while total != 0:
        test_next_number -= index
        nd_test = test_next_number - index - 1
        if test_next_number in summands:
            test_next_number += index
            index += 1
        elif nd_test < 0 and test_next_number != 0:
            while total != 0:
                index += 1
                if total == index:
                    summands.append(index)
                    return summands           
        else:
            total -= index
            summands.append(index)
            index += 1
    return summands
    



    

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')
