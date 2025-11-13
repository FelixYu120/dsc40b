from dsc40graph import UndirectedGraph
from collections import deque

def assign_good_and_evil(graph):
  labels = {} 
    
  for start_node in graph.nodes:
      
    if start_node in labels:
      continue

    q = deque([start_node])
    labels[start_node] = 'good'
    
    while q:
      current_node = q.popleft()
      current_label = labels[current_node]

      opposite_label = 'evil' if current_label == 'good' else 'good'

      for neighbor in graph.neighbors(current_node):
        if neighbor not in labels:
          labels[neighbor] = opposite_label
          q.append(neighbor)
            
        elif labels[neighbor] == current_label:
          return None
  return labels
