def cluster(graph, weights, level):
  visited = set()
  clusters = []
  
  # Retrieve all nodes from the graph to ensure we visit disconnected components.
  # Checks for 'adj' attribute (standard for dsc40graph) or 'nodes' attribute.
  all_nodes = []
  if hasattr(graph, 'adj'):
    all_nodes = list(graph.adj.keys())
  elif hasattr(graph, 'nodes'):
    all_nodes = list(graph.nodes)

  for start_node in all_nodes:
    if start_node not in visited:
      # Start a new cluster (connected component)
      current_cluster = set()
      # Use a stack for iterative DFS
      stack = [start_node]
      
      visited.add(start_node)
      current_cluster.add(start_node)
      
      while stack:
        u = stack.pop()
        
        # Get neighbors
        neighbors = []
        if hasattr(graph, 'adj'):
          neighbors = graph.adj.get(u, [])
        elif hasattr(graph, 'neighbors'):
          neighbors = graph.neighbors(u)
        
        for v in neighbors:
          if v not in visited:
            # Only traverse if the edge weight meets the level requirement
            if weights(u, v) >= level:
              visited.add(v)
              current_cluster.add(v)
              stack.append(v)
    
      clusters.append(frozenset(current_cluster))
        
  return frozenset(clusters)
