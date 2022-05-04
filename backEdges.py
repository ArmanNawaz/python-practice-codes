# Back Edges
# Aakash Sir
# 04 May 2022

def dfs(node, parent, visited, graph):
    visited[node] = True

    for nbr in graph[node]:
        if visited[nbr] == False:
            dfs(nbr, node, visited, graph)
        
        # If we found any backedge then print
        elif nbr != parent:
            print(node, "---> ", nbr)

def buildGraph(num_vertices, edges):
    graph = dict()

    for i in range(num_vertices):
        graph[i] = list()

    for edge in edges:
        graph[edge[0]].append(edge[1])
        graph[edge[1]].append(edge[0])

    return graph


def backEdges(edges, num_vertices, num_edges):
    graph = buildGraph(num_vertices, edges)

    visited = [False] * num_vertices

    dfs(0, -1, visited, graph)

if __name__ == '__main__':
    num_vertices = int(input())
    num_edges = int(input())

    edges = []
    for i in range(num_edges):
        edges.append(list(map(int, input().split())))
    
    backEdges(edges, num_vertices, num_edges)
