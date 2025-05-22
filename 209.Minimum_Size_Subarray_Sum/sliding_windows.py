class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # enumerate right boundary
        n = len(nums)
        ans = n + 1
        total = 0
        left = 0
        for right, v_r in enumerate(nums):
            total += v_r
            while total - nums[left] >= target:
                total -= nums[left]
                left += 1
            # total - nums[left] < target && total >= target
            if total >= target:
                ans = min(ans, right-left+1)
        return ans if ans <= n else 0           
