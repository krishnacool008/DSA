from collections import defaultdict, deque

def alienOrder(words):
    # Step 1: Create graph and indegree
    adj = defaultdict(set)

    # indegree = {c: 0 for word in words for c in word}
    indegree = {}
    for word in words:
        for c in word:
            indegree[c] = 0

    # Step 2: Build graph from adjacent words
    for i in range(len(words) - 1):
        w1, w2 = words[i], words[i+1]
        min_len = min(len(w1), len(w2))

        # Edge case: prefix violation
        if w1[:min_len] == w2[:min_len] and len(w1) > len(w2):
            return ""

        for j in range(min_len):
            if w1[j] != w2[j]:
                if w2[j] not in adj[w1[j]]:
                    adj[w1[j]].add(w2[j])
                    indegree[w2[j]] += 1
                break
    
    print(indegree)
    print(adj)

    # Step 3: Topological Sort (Kahn's algorithm)
    # queue = deque([c for c in indegree if indegree[c] == 0])
    queue = deque()
    for i in indegree:
        if indegree[i] == 0:
            queue.append(i)
        
    print(queue)
    res = []

    while queue:
        c = queue.popleft()
        res.append(c)
        for neighbor in adj[c]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)

    # If all characters are in result, return it
    # return ''.join(res) if len(res) == len(indegree) else ""
    if len(res) == len(indegree):
        return ''.join(res)
    else:
        return "" 


words=["wrt","wrf","er","ett","rftt","te"]
print(alienOrder(words))  # Possible output: "wertf"