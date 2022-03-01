# python3
import sys
import random

def compute_min_refills(distance, tank, stops):
    # write your code here
    stops.append(distance)
    index = 0
    starting_point = 0
    re_fuel = 0
    
    if distance <= tank:
        return 0
    for i in range(len(stops)+ 1):
        while index < len(stops):
            new_distance = stops[index]
            calculus = new_distance - starting_point
            if calculus  <= tank:
                index += 1  
            else:
                break
        if index == starting_point:
            return -1    
        if starting_point == distance:
            return re_fuel 
        if index < len(stops):
            re_fuel += 1
        starting_point = stops[index-1]  
    if distance != starting_point:
        return -1      

if __name__ == '__main__':
    d, m, _, *stops = map(int, sys.stdin.read().split())
    print(compute_min_refills(d, m, stops))
