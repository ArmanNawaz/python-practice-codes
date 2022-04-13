from collections import deque
def solve(graph, indegree, n, hrs):
    total_hrs = [0] * (n + 1)
    queue = deque()
    
    for key, value in indegree.items():
        if value == 0:
            total_hrs[key] = hrs[key]
            queue.append(key)
    
    while queue:
        currModule = queue.popleft()

        for nbr in graph[currModule]:
            if nbr != 0:
                queue.append(nbr)
                total_hrs[nbr] = total_hrs[currModule] + hrs[nbr]
                indegree[nbr] -= 1
                if indegree[nbr] == 0:
                  queue.append(nbr)

    return max(total_hrs)

if __name__ == '__main__':

    t = int(input())

    for test in range(t):
        n = int(input())

        graph = dict()
        indegree = dict()

        for i in range(n):
            graph[i + 1] = list()
            indegree[i + 1] = 0

        hrs = [0] * (n + 1)

        for _ in range(n):
            moduleInfo = list(map(int, input().split()))
            i = moduleInfo[0]
            hrs[i] = moduleInfo[1]
            modulePre = moduleInfo[2: ]

            for nbr in modulePre:
                if nbr != 0:
                    graph[nbr].append(i)
                    indegree[i] += 1

        ans = solve(graph, indegree, n, hrs)
        print(ans)
            


