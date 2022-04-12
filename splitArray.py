from math import gcd

def goodSplit(arr, n):
    dp = [0] * (n+1)

    for i in range(n-1, -1, -1):
        currbest = dp[i+1] + 1
        if(arr[i] != 1):
            for j in range(i+1, n):
                if gcd(arr[i], arr[j]) > 1:
                    currbest = min(currbest, dp[j+1] + 1)
        else:
            currbest -= 1
            
        dp[i] = currbest
    return dp[0]


if __name__ == '__main__':
    arr = [3, 5, 1, 7, 8, 20, 14, 28, 22, 361]
    n = len(arr)

    print(goodSplit(arr, n))