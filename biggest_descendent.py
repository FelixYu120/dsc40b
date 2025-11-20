def biggest_descendent(graph, root, value):
  biggest_values = {}

  def dfs(node):
    current_max = value[node]
    
    # Retrieve neighbors. 
    # Checks for 'adj' attribute (standard for dsc40graph) or 'neighbors' method.
    children = []
    if hasattr(graph, 'adj'):
      children = graph.adj.get(node, [])
    elif hasattr(graph, 'neighbors'):
      children = graph.neighbors(node)
        
    # Recursively find the max value in children's subtrees
    for child in children:
      child_max = dfs(child)
      if child_max > current_max:
        current_max = child_max
    
    # Store and return the result for this node
    biggest_values[node] = current_max
    return current_max

  dfs(root)
  return biggest_values
