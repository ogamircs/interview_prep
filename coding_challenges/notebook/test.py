from heapq import heappush, heappop
from collections import deque

def quickestWayUp(ladders, snakes):
    BOARD_SIZE = 10
    DICE_ROLL = [i for i in range(1,7)]
    shortest_path = []
    #build adjecensy matrix
    adj_matrix = {i:[] for i in range(BOARD_SIZE)}
    for i in range(BOARD_SIZE-1):
        next = i+1
        if(next<BOARD_SIZE-1):
            adj_matrix[i].append(next)
        else:
            adj_matrix[i].append(BOARD_SIZE-1)
    for e in ladders:
        adj_matrix[e[0]-1].append(e[1]-1)
    for e in snakes:
        adj_matrix[e[0]-1].append(e[1]-1)

    for DICE in DICE_ROLL:
        #now do a BFS from 0 to 100
        out = [-1] * BOARD_SIZE # Distances array, -1 for unreachable nodes
        visited = set()
        queue = deque([0])
        while queue:
            current = queue.popleft()
            visited.add(current)
            for neighbor in adj_matrix[current]:
                if ((neighbor not in visited) and (abs(neighbor-current)==DICE)):
                    visited.add(neighbor)
                    queue.append(neighbor)
                    out[neighbor] = out[current] + 1 
        heappush(shortest_path,out[BOARD_SIZE-1])

    print(shortest_path)
    return heappop(shortest_path)

quickestWayUp([[2,4]],[[6,1]])