
def solve(arr, i, ans, dp):
	if i >= len(arr)-2:
		return ans+2

	if dp[i] != -1: return dp[i]
	if max(arr[i], arr[i+1]) <= max(arr[i+1], arr[i+2]):
		ans = max(1 + solve(arr, i + 1, ans, dp), ans)
		dp[i] = ans
		
	else:
		ans = max(solve(arr, i + 1, ans, dp), ans)
		dp[i] = ans
	return ans



arr = [70,66,32,60,51,75,35,88,98,64]
n = len(arr)
ans  = 0
dp = [-1] * (n+1)
print (solve(arr, 0, ans, dp))

