class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # i < j < k
        ans = []
        nums = sorted(nums)
        n = len(nums)
        for i in range(n-2):
            j = i + 1
            k = n - 1
            if i > 0 and nums[i] == nums[i-1]:
                continue
            # 优化1
            if nums[i] + nums[i+1] + nums[i+2] > 0:
                break
            # 优化2
            if nums[i] + nums[n-1] + nums[n-2] < 0:
                continue
            while j < k: # j, k 等于两数之和的left， right
                s = nums[j] + nums[k]
                if s < -nums[i]:
                    j += 1
                elif s > -nums[i]:
                    k -= 1
                else:
                    ans.append((nums[i], nums[j], nums[k]))
                    j += 1
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                    k -= 1
                    while k > j and nums[k] == nums[k + 1]:
                        k -= 1
        return ans
            

