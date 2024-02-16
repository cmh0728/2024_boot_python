import sys
input = sys.stdin.readline

def fibonachi(n):
    dp = [0]*(n+1)
    if n == 1 or n == 2:
        return 1
    else:
        dp[1] = 1
        dp[2] = 1
        for i in range(3,n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]

print(f"답 : {fibonachi(31)}")
    