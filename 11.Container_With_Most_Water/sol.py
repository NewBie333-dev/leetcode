class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        ans = 0
        while l < r:
            area = (r - l) * min(height[r], height[l])
            ans = max(ans, area)
            if height[l] < height[r]:
                l += 1
            else:   # 包括等于
                r -= 1
        return ans
