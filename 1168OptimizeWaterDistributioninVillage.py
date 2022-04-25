# 1168. Optimize Water Distribution in a Village
# Prims Algorithm
from heapq import *

def primsMST(graph, vertices):  
    temp = (0, 0) # node, cost, source = 0
    minHeap = []
    # Heap is made on the basis of cost/weight
    heappush(minHeap, (temp[1], temp))

    distance = [float('inf')] * vertices
    visited = [False] * vertices
    distance[0] = 0

    while len(minHeap):
        tup = heappop(minHeap)
        
        node = tup[1][0]
        
        for nbr in range(vertices):
            # graph[node][nbr] = 0 means there is no edge b/w node and nbr
            if visited[nbr] == False and graph[node][nbr] != -1:
                if distance[nbr] > graph[node][nbr]:
                    distance[nbr] = graph[node][nbr]
                    heappush(minHeap, (distance[nbr], (nbr, distance[nbr])))
        visited[node] = True
    # print(distance)
    # Return MST Cost
    return sum(distance)

def buildGraph(n, wells, pipes):
    graph = [[-1] * (n + 1) for _ in range(n + 1)]

    for pipe in pipes:
        house1 = pipe[0]
        house2 = pipe[1]
        cost = pipe[2]

        graph[house1][house2] = cost
        graph[house2][house1] = cost

    for i in range(n):
        graph[0][i + 1] = wells[i]
        graph[i + 1][0] = wells[i]
    
    return graph

if __name__ == '__main__':
    n = 3
    wells = [1,2,2]
    pipes = [ [1, 2, 1], [2 , 3, 1]]
    graph = buildGraph(n, wells, pipes)
    print(primsMST(graph, n + 1))