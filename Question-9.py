def dfs_recursive(graph, current_node, visited=None):
    if visited is None:
        visited = set()

    # Mark the current node as visited and process it
    visited.add(current_node)
    print(current_node, end=" ")

    # Recur for all unvisited adjacent vertices
    for neighbor in graph.get(current_node, []):
        if neighbor not in visited:
            dfs_recursive(graph, neighbor, visited)

    return visited


# Example Graph (Adjacency List)
graph = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F"],
    "D": [],
    "E": ["F"],
    "F": [],
}

print("Recursive DFS Traversal:")
dfs_recursive(graph, "A")
# Output: A B D E F C
