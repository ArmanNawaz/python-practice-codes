# from math import gcd

# def LXCPS(N,A, M, B):
#     ans = 0
#     for i in range(N):
#         if A[i] == 1:
#             continue
#         flag = True
#         for j in range(M):
#             x = gcd(A[i], B[j])
#             if x != 1:
#                 flag = False
#                 break
#         if flag:
#             ans += 1
#     if ans == 0:
#         return -1
#     return ans



# a = [2,3,5,6,7,1,2,5,6,7]
# b = [2,3,4,5,6]
# print(LXCPS(len(a), a, len(b), b))


# n = int(input())
# m = int(input())
# a = []
# b = []
# for i in range(n):
#     a.append(int(input()))
# for i in range(n):
#     b.append(int(input()))
# n = 3
# m = 3
# a= [-3, 5, 1]
# b = [3, -3, -1]
# a.sort(reverse=True)
# b.sort(reverse=True)
# mi = a[0]
# su = 0
# for i in range(1,m):
#     mi = min(mi,a[i])
# for i in range(m):
#     su = su + b[i]
# print((mi*su)%1000000007)


from heapq import *

def third_max_score(A, B):
    scores = []
    for i in range(3):
        heappush(scores, (A[i] * B[i], B[i], i))
    for i in range(3, len(A)):
        score = A[i] * B[i]
        if score > scores[0][0]:
            heappop(scores)
            heappush(scores, (score, B[i], i))
        elif score == scores[0][0] and B[i] > scores[0][1]:
            heappop(scores)
            heappush(scores, (score, B[i], i))
        elif score == scores[0][0] and B[i] > scores[0][1] and i > scores[0][2]:
            heappop(scores)
            heappush(scores, (score, B[i], i))
    return scores[0][2]
# a= [-3, 5, 1]
# b = [3, -3, -1]
# a =[-4,-1,-5,5,-2]
# b=[0,-1,3,-1,4]
a=[-5,-5,3,2,0]
b=[-3,1,1,-5,-5]
third_max_score(a, b)