[题目](https://leetcode.cn/problems/two-sum/?envType=study-plan-v2&envId=top-100-liked)
### Hash Table
哈希表是一种高效的数据结构，用于存储**键值对(key-value pairs)**。它通过哈希函数(hash function)将键(key)映射到表中的特定位置，从而实现快速的数据访问。

```
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        idx = {}  # 创建一个空哈希表（字典）
        for j, x in enumerate(nums):  # x=nums[j]
            if target - x in idx:  # 在左边找 nums[i]，满足 nums[i]+x=target
                return [idx[target - x], j]  # 返回两个数的下标
            idx[x] = j  # 保存 nums[j] 和 j

作者：灵茶山艾府
链接：https://leetcode.cn/problems/two-sum/solutions/2326193/dong-hua-cong-liang-shu-zhi-he-zhong-wo-0yvmj/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
```

相比暴力做法，哈希表多消耗了内存空间，但减少了运行时间，这就是「空间换时间」。

很多涉及到「两个变量」的题目，都可以枚举其中一个变量，把它当成常量看待，从而转换成「一个变量」的问题。

代码实现时，通常来说「枚举右，寻找左」是更加好写的。

Hash Table: **从一堆数中，找一个数**

注意这里`if target - x in idx:  # 在左边找 nums[i]，满足 nums[i]+x=target` 我们这里是枚举j而不是枚举i


