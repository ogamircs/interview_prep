from heapq import heappush, heappop
from collections import deque

def bfs(n, m, edges, s):
    #build adjacency matrix
    adj_matrix = {i: [] for i in range(0,n)}
    for e in edges:
        adj_matrix[e[0]].append(e[1])
        adj_matrix[e[1]].append(e[0])
    print(adj_matrix)
    #now bfs through adj matrix
    out = [-1] * n  # Distances array, -1 for unreachable nodes
    visited = set()
    queue = deque([s]) 
    out[s - 1] = 0
    # Step 3: Perform BFS
    while queue:
        current = queue.popleft()
        visited.add(current)

        # Traverse neighbors using a for loop
        for neighbor in adj_matrix[current]:
            if neighbor not in visited:  # Only visit unvisited nodes
                visited.add(neighbor)
                queue.append(neighbor)
                out[neighbor - 1] = out[current - 1] + 6  # Increment distance by weight (6)
    zero_ind = out.index(0)
    return out[0:zero_ind]+out[zero_ind+1:n]


bfs(5,6,[[0,1],[0,2],[1,2],[1,3],[2,4],[3,4]],0)