class Solution:
    def climbStairs(self, n: int) -> int:
        m = {}
        def dfs(n):
            if n in m:
                return m[n]
            if n == 1:
                m[n] = 1
            elif n == 2:
                m[n] = 2
            else:
                m[n] = dfs(n - 1) + dfs(n - 2)
            return m[n]
        
        return dfs(n)
