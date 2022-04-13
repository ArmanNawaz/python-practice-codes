# Problem Statement:
# TCS is working on a new project called “Testvita“. There are N modules in the project. Each module i has a completion time denoted in the number of hours Hi and may depend on other modules. If module x depends on module y then one needs to complete y before x.

# As a project manager, you are asked to deliver the project as early as possible. Provide an estimation of the amount of time required to complete the project.

# Input Format:
# The first line contains T, the number of test cases.
# For each test case:

# The first line contains N, the number of modules.
# Next N lines, each contains:
# i – module id
# Hi – number of hours it takes to complete the module
# D – set of module ids that i depends on – integers delimited by space
# Output Format:
# Output the minimum number of hours required to deliver the project.

# Constraints:
# 1 <= T <= 10
# 0 < N < 1000; number of modules
# 0 < i <= N; module Id
# 0 < Hi < 60; number of hours it takes to complete the module i
# 0 <= |D| < N; number of dependencies
# 0 < Dk <= N; module Id of dependencies

# Example 1:
# Input:
# 1
# 5
# 1 5 0
# 2 6 1
# 3 3 2
# 4 2 3
# 5 1 3

# Output:
# 16


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
            


