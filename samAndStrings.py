def solve(n):
    dp = [int(n[0])]
    temp = int(n[0])

    for i in range(1, len(n)):
        temp = (i+1) * int(n[i]) + 10 * dp[i-1]
        dp.append(temp)
    # print(dp)
    return sum(dp)

def solve2(num):
    ans = 0
    n = len(num)
    for i in range(n):
        temp = num[i] * (n - i)
        ans += int(temp) * (i+1)
    return ans


if __name__ == '__main__':
    n = input()

    print(solve2(n))