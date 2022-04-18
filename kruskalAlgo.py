from DSU import findSet, unionSet

def kruskalMst(edges, vertices):
    ans = 0
    parent = [-1] * (vertices + 1)
    edges.sort(key = lambda x: x[2]) # Sort edges according to weight

    for edge in edges:
        u, v, w = edge

        lp_u = findSet(u, parent)
        lp_v = findSet(v, parent)

        if lp_u != lp_v:
            unionSet(u, v, parent)
            ans += w
    return ans

if __name__ == '__main__':

    # edges = [u, v, cost]
    edges = [[1, 2, 1],
             [1, 3, 2],
             [1, 4, 2],
             [2, 3, 2],
             [2, 4, 3],
             [1, 4, 3]]
    
    vertices = len(edges)
    print(kruskalMst(edges, vertices))
    
