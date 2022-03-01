# Uses python3
import sys
from operator import itemgetter

def get_optimal_value(capacity, weights, values):
    value = 0.
    total_weight = capacity
    # write your code here
    dictio = {}
    values_weights = []
    for i in range(len(values)):
        dictio["value"] = values[i]
        dictio["weights"] = weights [i]
        dictio["v/w"] = values[i] / weights [i]
        values_weights.append(dictio)
        dictio = {}
    order_list = sorted(values_weights, key=itemgetter('v/w'), reverse=True)
    for i in range(len(values)):
        if total_weight == 0:
            return value
        if total_weight >= order_list[i]["weights"]:
            value += order_list[i]["value"]
            total_weight -= order_list[i]["weights"]
        else:
            a = total_weight / order_list[i]["weights"]
            value += (a * order_list[i]["value"])
            total_weight -= a * order_list[i]["weights"]
    return value



if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
    
