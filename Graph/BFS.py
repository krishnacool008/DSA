from collections import deque


def bfs(graph, start):
    visited = set()
    queue = deque()

    visited.add(start)  # Visited first node i.e start
    print(start)  # Printed out first visited node

    # After visiting the node added it to queue
    # So, That now we can visit it's Neighbours
    queue.append(start)

    while queue:
        # Got the node for which we want to visit Neighbours
        node = queue.popleft()

        # Visiting all the Neighbour for the node
        for neighbor in graph[node]:

            # If we havnt visited this node
            # Than add it to visited
            # Add it to queue cuz we now want to visit it's Neighbours
            if neighbor not in visited:
                visited.add(neighbor)
                print(neighbor, end=' ')
                queue.append(neighbor)
        print()

# Example usage
graph = {
    1: [2, 4],
    2: [3],
    3: [4],
    4: []
}
bfs(graph, 1)
