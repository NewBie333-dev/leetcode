class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for j, v_j in enumerate(nums):
            if (target - v_j) in dic:
                return (j, dic[target - v_j])
            dic[v_j] = j

