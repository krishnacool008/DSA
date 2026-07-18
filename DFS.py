
# This recusive method is 
# Visiting the first node and visitng neighbour nodes
def dfs(graph, start, visited):

    # Visit first node
    visited.add(start)
    print(start, end=" ")

    # Visit neighbours
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

# Example usage
graph = {
    1: [2, 4],
    2: [3],
    3: [4],
    4: []
}

visited = set()

# Pass visited set
dfs(graph, 1, visited)
