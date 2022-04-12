def solve(arr, cost):
    n = len(arr)
    dp = [0] * (n+1)
    dp[1] = cost

    for i in range(2, n+1):
        dp[i] = dp[i - 1] + cost
        hashMap = dict()
        argument = 0
        for j in range(i, 0, -1):
            hashMap[arr[j-1]] = hashMap.get(arr[j-1], 0) + 1
            if hashMap[arr[j-1]] == 2:
                argument += 2
            elif hashMap[arr[j-1]] > 2:
                argument += 1
            dp[i] = min(cost + argument + dp[j - 1], dp[i])


    return dp[n]

if __name__ == '__main__':
    arr = [2, 4, 4, 2, 1, 5]
    cost = 3
    print(solve(arr, cost))

