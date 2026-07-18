from collections import deque

class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

def cloneGraph(node: Optional['Node']) -> Optional['Node']:
    if not node:
        return
    
    visited = {}
    clone = Node(node.val)
    visited[node] = clone
    queue = deque()
    queue.append(node)

    while queue:
        node = queue.popleft()
        for neighbour in node.neighbors:
            if neighbour not in visited:
                visited[neighbour] = Node(neighbour.val)
                queue.append(neighbour)
            visited[node].neighbors.append(visited[neighbour])

    return clone


# Function to print the graph (for testing purposes)
def print_graph(node, visited=None):
    if visited is None:
        visited = set()
    if node in visited:
        return
    visited.add(node)
    print(f'Node {node.val} with neighbors {[neighbor.val for neighbor in node.neighbors]}')
    for neighbor in node.neighbors:
        print_graph(neighbor, visited)

# Build a graph with 4 nodes
# 1 -- 2
# |    |
# 4 -- 3
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)

node1.neighbors.append(node2)
node1.neighbors.append(node4)
node2.neighbors.append(node3)
node3.neighbors.append(node4)


cloned = cloneGraph(node1)

print("Original graph:")
print_graph(node1)
print("\nCloned graph:")
print_graph(cloned)