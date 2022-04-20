from heapq import *

def build_graph(v, edges):
    graph = dict()

    # Assume vertices are 1 to v
    for vertex in range(v + 1):
        graph[vertex] = list()
    
    for edge in edges:
        graph[edge[0]].append(edge[1])

    return graph

def build_cost(edges):
    cost = dict()

    for edge in edges:
        cost[(edge[0], edge[1])] = edge[2]
    
    return cost


def dijkstra(v, edges):
    graph = build_graph(v, edges)
    cost = build_cost(edges)

    # Assume source to be 1
    src = 1
    dist = [float('inf')] * (v + 1)
    parent = [-1] * (v + 1)
    visited = [False] * (v + 1)

    minHeap = []
    heappush(minHeap, (0, src))

    dist[src] = 0

    while minHeap:
        currDist, currNode = heappop(minHeap)

        if visited[currNode] == False:
            visited[currNode] = True
            
            for nbr in graph[currNode]:
                if currDist + cost[(currNode, nbr)] < dist[nbr]:
                    dist[nbr] = currDist + cost[(currNode, nbr)] 
                    parent[nbr] = currNode
                    heappush(minHeap, (dist[nbr], nbr))

    # print(parent)
    return dist


if __name__ == '__main__':
    # Number of vertices and edges
    v, e = list(map(int, input().split()))
    edges = []

    for i in range(e):
        src, dest, wt = list(map(int, input().split()))
        edges.append([src, dest, wt])
    
    # Distance array
    ans = dijkstra(v, edges)
    print(ans[1: ])