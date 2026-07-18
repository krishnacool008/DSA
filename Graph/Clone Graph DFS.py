from collections import deque
from typing import Optional

class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


def cloneGraph(node: Optional['Node']) -> Optional['Node']:
    if not node:
        return None

    visited = {}
    queue = deque()
    node_1 = Node(node.val)
    visited[node] = node_1
    queue.append(node)

    while queue:
        node = queue.popleft()
        for neighbour in node.neighbors:
            if neighbour not in visited:
                # Clone the neighbour and put in the visited dictionary
                # In queue we only add new node to prevent if prevenet infinite loop
                visited[neighbour] = Node(neighbour.val)
                queue.append(neighbour)
            # We have to add neighour no matter we visited it or not
            # Visited neighbour can also be a neighbour of current node, 
            # so we have to add it to the neighbours list of current node
            visited[node].neighbors.append(visited[neighbour])
    return node_1



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
