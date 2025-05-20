class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ans = 0
        set_nums = set(nums)
        for n in set_nums:
            if n - 1 in set_nums: # 证明n不是起始值，跳过
                continue
            y = n + 1             # 判断n+1在不在set中，如果在继续判断n+2在不在set中 ... etc...
            while y in set_nums:
                y += 1
            cur_len = y - n
            ans = max(cur_len, ans)
        return ans

# 为什么是O(n)的复杂度：
# O(n)，其中 n 是 nums 的长度。在二重循环中，每个元素至多遍历两次：在外层循环中遍历一次，在内层循环中遍历一次。所以二重循环的时间复杂度是 O(n) 的。比如 nums=[1,2,3,4]，其中 2,3,4 不会进入内层循环，只有 1 会进入内层循环。

