# This recursive method is
# Visiting the first node and visiting neighbour nodes
def dfs(graph, start, visited):
	# Visit first node
	visited.add(start)
	print(start)

	# Visit neighbours
	for neighbor in graph[start]:
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
