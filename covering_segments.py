# Uses python3
import sys
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')

def optimal_points(segments):
    points = []
    #write your code here
    for s in segments:
        test_list = [s.start , s.end]
        points.append(test_list)
    
    result = []
       
    while len(points) != 0:
        most_left = points[0][0]
        right_point = points[0][1]
        list_to_delete = []
        tracking_seg = 0
        index = 0
        #Get most left point
        for i in range(len(points)):
            if most_left > points[i][0] and right_point > points[i][1] or most_left < points[i][0] and right_point > points[i][1]:
                most_left = points[i][0]
                right_point = points[i][1]
        for i in range(len(points)):
            if right_point <= points[i][1] and right_point >= points[i][0]:
                tracking_seg += 1 
                index = i
                list_to_delete.append(i)
                result.append(right_point)
        for i in reversed(list_to_delete):
            points.pop(i)        
        #If segment is alone, append it and del it        
        if tracking_seg == 0:
            result.append(right_point)
            del(points[index])             
    return list(dict.fromkeys(result))

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    print(*points)
