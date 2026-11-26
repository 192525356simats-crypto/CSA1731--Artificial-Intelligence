from collections import deque

def bfs(graph, start_node):
    visited = set([start_node])
    queue = deque([start_node])
    traversal_order = []

    while queue:
        # Remove the oldest node from the front of the queue
        current_node = queue.popleft()
        traversal_order.append(current_node)

        # Explore all unvisited neighbors
        for neighbor in graph.get(current_node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return traversal_order

# Example graph represented as an adjacency list
sample_graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

# Run BFS starting from node 'A'
result = bfs(sample_graph, 'A')
print("BFS Traversal Order:", result)
