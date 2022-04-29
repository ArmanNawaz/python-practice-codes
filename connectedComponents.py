# Given a graph. Find all the connected components in
# the graph.

def buildGraph(edges, vertices):
    graph = dict()

    for i in range(vertices):
        graph[i] = list()
    
    for edge in edges:
        graph[edge[0]].append(edge[1])
        graph[edge[1]].append(edge[0])
    return graph

def dfs(graph, node, visited, temp):
    visited[node] = True
    temp.append(node)
    
    for nbr in graph[node]:
        if visited[nbr] == False:
            dfs(graph, nbr, visited, temp)
            
    return temp

def findComponents(edges, vertices):
    graph = buildGraph(edges, vertices)
    visited = [False] * vertices
    ans = []
    for i in range(vertices):
        temp = []
        if visited[i] == False:
            ans.append(dfs(graph, i, visited, temp))
    return ans
    


if __name__ == '__main__':
    edges = [[0, 1], [1, 2],
             [3, 4],
             [5, 6], [6, 7], [6, 8]]
    
    vertices = 9

    print(findComponents(edges, vertices))