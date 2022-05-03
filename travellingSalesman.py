# Aakash Sir
# 03 May 2022
# Travelling Salesman Problem
# Here visited array is maintained using bitmask

def tsp(cities, visited, city, n, dp):
    
    # if we are at last city then return cost of
    # last city to first
    if visited == ((1 << n) - 1):
        return cities[city][0]
    
    if dp[visited][city] != -1:
        return dp[visited][city]

    finalCost = float('inf')

    # iterate for each city
    for i in range(0, n):
        # If current city is not visited for current branch
        if (visited & (1 << i)) == 0:
            tempAns = cities[city][i] + tsp(cities, visited | (1 << i), i, n, dp)
            finalCost = min(finalCost, tempAns)

    dp[visited][city] = finalCost
    return finalCost


if __name__ == '__main__':
    cities = [[0, 20, 42, 25],
              [20, 0, 30, 34],
              [42, 30, 0, 10],
              [25, 34, 10, 0]]

    n = 4
    dp = [[-1] * n for _ in range(1<<n)]
    ans = tsp(cities, 1, 0, n, dp)
    print(ans)