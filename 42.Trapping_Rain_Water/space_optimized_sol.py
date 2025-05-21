class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left = 0
        right = n - 1
        suf_max = 0
        pre_max = 0
        ans = 0
        while left <= right:    #  =依然可以算相等的值
            pre_max = max(pre_max, height[left])
            suf_max = max(suf_max, height[right])
            if pre_max < suf_max:
                ans += pre_max - height[left]
                left += 1
            else:   # 相等的情移动哪一个都行
                ans += suf_max - height[right]
                right -= 1
        return ans
