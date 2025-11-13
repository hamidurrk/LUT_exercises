def jumps(n, a, b):
	dp = [0] * (n + 1)
	dp[0] = 1
	for i in range(n + 1):
		if i + a <= n:
			dp[i + a] += dp[i]
		if i + b <= n:
			dp[i + b] += dp[i]
	return dp[n]

if __name__ == "__main__":
	print(jumps(4, 1, 2))
	print(jumps(8, 2, 3))
	print(jumps(11, 6, 7))
	print(jumps(30, 3, 5))
	print(jumps(100, 4, 5))
