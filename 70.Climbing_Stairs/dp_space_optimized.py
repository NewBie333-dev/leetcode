class Solution:
    def climbStairs(self, n: int) -> int:
        left_node = 2
        right_node = 1
        root = 0
        if n == 1:
            return 1
        if n == 2:
            return 2
        for i in range(3,n+1):
            root = left_node + right_node
            right_node = left_node
            left_node = root
        return root
