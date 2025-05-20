class Solution:    
    def climbStairs(self, n: int) -> int:
        def dfs(n):
            if n == 1:
                return 1
            elif n == 2:
                return 2
            else:
                return dfs(n - 1) + dfs(n - 2)
        return dfs(n)
