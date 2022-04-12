# Prime Counters – TCS Codevita 2017 – Round 2

# Problem Statement:
# Given a number N, let CP(N) denote the number of primes between 1 and N (inclusive of N). We call N a prime counter if CP(N) is a prime (N need not be a prime). 
# For example, CP(3) = 2, CP(4) = 2, CP(5) = 2, CP(7) = 4.

# Input Format:
# First-line contains an integer T, a number of test cases. Next T lines each containing two positive integers L, R separated by space.

# Output Format:
# T lines containing the number of prime counters between L and R (both inclusive) in the ith test case (or NONE is no prime counter exists in that range).

# Constraints:
# L ≤ R ≤ 106

def solve(queries, n):
    prime = [True] * (n + 1)
    cp = [0] * (n + 1)
    primeCounter = [0] * (n + 1)

    prime[0], prime[1] = False, False

    for number in range(2, n + 1):
        cp[number] = cp[number - 1]
        primeCounter[number] = primeCounter[number - 1]

        if prime[number]:
            cp[number] += 1
        
        if prime[cp[number]]:
            primeCounter[number] += 1

        # Filling Seive Array
        if prime[number]:
            for multiple in range(number * number, n + 1, number):
                prime[multiple] = False
    print(prime)
    print(cp)
    print(primeCounter)
    for each in queries:
        l, r = each[0], each[1]
        ans = primeCounter[r] - primeCounter[l - 1]

        if ans == 0:
            print("None")
        else:
            print(ans)

if __name__ == '__main__':
    t = int(input())
    queries = []
    maxNumber = 0

    for _ in range(t):
        l, r = list(map(int, input().split()))
        queries.append([l, r])

        maxNumber = max(maxNumber, r)
    solve(queries, maxNumber)