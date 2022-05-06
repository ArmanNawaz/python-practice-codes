# 06 May 2022
# Aakash sir
# Bridges


def dfs(node, parent, vis, dis, low, graph, bridges, timer):
    vis[node] = True
    dis[node] = timer
    low[node] = timer
    timer += 1

    for nbr in graph[node]:
        if nbr == parent:
            continue
        elif vis[nbr] == False:
            dfs(nbr, node, vis, dis, low, graph, bridges, timer)
            low[node] = min(low[node], low[nbr])
            if low[nbr] > dis[node]:
                bridges.append([node, nbr])
        else:
            low[node] = min(low[node], dis[nbr])


def buildGraph(edges, vertices):
    graph = dict()

    for i in range(vertices):
        graph[i] = list()

    for edge in edges:
        graph[edge[0]].append(edge[1])
        graph[edge[1]].append(edge[0])
    return graph

def findBridges(edges, vertices):
    visited = [False] * vertices
    discoveryTime = [0] * vertices
    lowestTime = [0] * vertices
    bridges = list()

    graph = buildGraph(edges, vertices)
    timer = 0
    for node in range(vertices):
        if visited[node] == False:
            dfs(node, -1, visited, discoveryTime, lowestTime, graph, bridges, timer)
   
    return bridges



if __name__ == '__main__':
    edges = [[0, 1], [0, 2], [1, 2], [1, 3], [3, 4], [3, 6], [4, 5], [5, 6]]
    vertices = 7

    ans = findBridges(edges, vertices)
    print(ans)