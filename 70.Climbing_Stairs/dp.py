class Solution:
    def climbStairs(self, n: int) -> int:
        f = {}
        f[1] = 1
        f[2] = 2
        for i in range(3,n+1):
            f[i] = f[i-1] + f[i-2] # 递推公式和dfs的递推公式完全一样
        return f[n]
