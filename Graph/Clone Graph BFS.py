class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
        

def cloneGraph(node: 'Node', visited: dict) -> 'Node':
    if not node:
        return None

    # Create a new node with the same value
    clone = Node(node.val)
    visited[node] = clone

    # Recursively clone all neighbors
    for neighbor in node.neighbors:
        # Now in dfs all the neighbour will be appended to clone negibours list
        # Note: "cloneGraph(neighbor, visited)" this will only append the first node ie "neighbor"
        # dfs also return the fist node copy which we are passing in param
        # So in both if and else we are appending neighbour copy
        if neighbor not in visited:
            # Clone we created on line 12
            clone.neighbors.append(cloneGraph(neighbor, visited)) 
        else:
            # Clone we created on line 13
            # Here we use visited instead of clonegraph because we already visited neighbor
            # And we have already created copy of neighbor and stored in visited dict
            # Plus calling dfs on visited node again will cause infinite loop
            # If we remove this else part it wil not add the neighbour which are already visited
            # We can have same neighbour to 2 different node
            clone.neighbors.append(visited[neighbor]) 
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

visited = {}
cloned = cloneGraph(node1, visited)

print("Original graph:")
print_graph(node1)
print("\nCloned graph:")
print_graph(cloned)
