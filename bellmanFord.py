def bellmanFord(edges, vertices, source):
    
    distance = [float('inf')] * (vertices + 1)
    distance[source] = 0
    
    for i in range(vertices - 1):
        for edge in edges:
            src, dest, wt = edge
            if distance[src] + wt < distance[dest]:
                distance[dest] = distance[src] + wt

    for edge in edges:
        src, dest, wt = edge
        if distance[src] + wt < distance[dest]:
            return "Negative cycle"

    return distance[1:]


if __name__ == '__main__':
    # vertices = 6
    # [src, dest, weight]
    # edges = [[1, 2, 6],
    #          [1, 3, 4],
    #          [1, 4, 5],
    #          [2, 5, -1],
    #          [3, 5, 3],
    #          [4, 3, -2],
    #          [4, 6, -1],
    #          [5, 6, 3],
    #          [3, 2, -2]
    #         ]

    vertices = 4
    edges = [[1, 2, 4],
             [1, 3, 5],
             [2, 4, 7],
             [4, 3, -15],
             [3, 2, 7]
            ]
    ans = bellmanFord(edges, vertices, 1)
    print(ans)