def solve(string):
    dp = [0] * (len(string) + 1)

    dp[1] = 1

    for i in range(2, len(dp)):
        if string[i - 1] != '0':
            dp[i] = dp[i - 1] + 1
        digit = int(string[i - 2: i])
        if digit >= 10 and digit <= 26:
            dp[i] += dp[i - 1]
    return dp[len(string)]

if __name__ == '__main__':
    string = "2226"
    print(solve(string))