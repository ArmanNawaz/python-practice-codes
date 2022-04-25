# Prims Algorithm
from heapq import *

def primsMST(graph, vertices):  
    temp = (0, 0) # node, cost
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

if __name__ == '__main__':
    # Graph is adjacency matrix
    # graph = [[-1, 4, 6, -1, -1, -1],
    #         [4, -1, 6, 3, 4, -1],
    #         [6, 6, -1, 1, -1, -1],
    #         [-1, 3, 1, -1, 2, 3],
    #         [-1, 4, -1, 2, -1, 7],
    #         [-1, -1, -1, 3, 7 ,-1]]
    # vertices = 6
    graph = [[-1, 1, -1, 0],
             [1, -1, 1, 0],
             [0, 1, -1, 3],
             [0, -1, 3, -1]]
    vertices = 4

    print(primsMST(graph, vertices))