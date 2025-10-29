import random

def knn_distance(arr, q, k):
    distances = [(abs(x - q), x) for x in arr]

    def quickselect(lst, k):
        if len(lst) == 1:
            return lst[0]
        
        pivot = random.choice(lst)[0]
        lows = [x for x in lst if x[0] < pivot]
        highs = [x for x in lst if x[0] > pivot]
        pivots = [x for x in lst if x[0] == pivot]

        if k <= len(lows):
            return quickselect(lows, k)
        elif k <= len(lows) + len(pivots):
            return pivots[0]
        else:
            return quickselect(highs, k - len(lows) - len(pivots))

    kth_distance, kth_value = quickselect(distances, k)
    return kth_distance, kth_value
