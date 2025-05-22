# this solution exceed time limits
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # brute force
        n = len(nums)
        ans = n + 1
        for left in range(n):
            right = left
            total = 0
            while right < n:
                total += nums[right]
                if total < target:
                    right += 1
                else:
                    if right - left + 1 < ans:
                        ans = right - left + 1
                    break
        return ans if ans != n + 1 else 0
                

