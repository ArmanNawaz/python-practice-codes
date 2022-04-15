# Disjoint Set Union

def findSet(node, parent):
    if parent[node] == -1:
        return node
    return findSet(parent[node], parent)

def unionSet(u, v, parent):

    # This is condition is only for undirected graph
    # This also implements Union by Rank in undirected graph
    if u > v:
        u, v = v, u

    leaderParent_u = findSet(u, parent)
    leaderParent_v = findSet(v, parent)

    if leaderParent_u != leaderParent_v:
        parent[leaderParent_v] = leaderParent_u


if __name__ == '__main__':
    edges = [[0, 1], [1, 2], [1, 3], [2, 3], [2, 5], [3, 5], [4, 6]]
    vertices = 7
    parent = [-1] * vertices

    for edge in edges:
        unionSet(edge[0], edge[1], parent)
    
    print(parent)