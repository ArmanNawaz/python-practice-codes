def rodCutting(P, n):
    if n == 0: return 0
    maxVal = -999999
    for i in range(1, n+1):
        maxVal = max(maxVal, P[i-1], rodCutting(P, n-i))
    return maxVal

P = [1, 5, 8, 9, 10, 17, 17, 20]
n = len(P)
print(rodCutting(P, n))