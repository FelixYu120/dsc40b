def knn_distance(arr, q, k):
  target_rank = k - 1 
  low = 0
  high = n - 1

  def partition_by_distance(arr, low, high, q):
    pivot_index = random.randint(low, high)
    pivot_distance = abs(arr[pivot_index] - q)

    arr[pivot_index], arr[high] = arr[high], arr[pivot_index]
    
    i = low 
    
    for j in range(low, high):
      current_distance = abs(arr[j] - q)
      if current_distance <= pivot_distance:
        arr[i], arr[j] = arr[j], arr[i]
        i += 1
            
    arr[i], arr[high] = arr[high], arr[i]
    return i

  while True:
    pivot_final_index = partition_by_distance(arr, low, high, q)
    
    if pivot_final_index == target_rank:
      kth_closest_point = arr[pivot_final_index]
      distance = abs(kth_closest_point - q)
      return (distance, kth_closest_point)
        
    elif pivot_final_index < target_rank:
      low = pivot_final_index + 1
    else: 
      high = pivot_final_index - 1
