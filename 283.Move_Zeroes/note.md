## sol 1 in place stack
在 Python 中，通常不建议在循环过程中直接修改正在被迭代的对象（比如 list），因为这可能会导致意外的行为。但在你的代码中，你并没有直接修改 nums 的长度或结构，而是修改了其中的元素值，所以这是安全的。

```
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        stack_size = 0
        for x in nums:
            if x:
                nums[stack_size] = x  # 把 x 入栈
                stack_size += 1
        for i in range(stack_size, len(nums)):
            nums[i] = 0

作者：灵茶山艾府
链接：https://leetcode.cn/problems/move-zeroes/solutions/2969353/kuai-man-zhi-zhen-wei-shi-yao-ke-yi-ba-s-1h8x/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
```


## sol 2 two pointer
```
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        i0 = 0
        for i in range(len(nums)):
            if nums[i]:
                nums[i], nums[i0] = nums[i0], nums[i]
                i0 += 1

作者：灵茶山艾府
链接：https://leetcode.cn/problems/move-zeroes/solutions/2969353/kuai-man-zhi-zhen-wei-shi-yao-ke-yi-ba-s-1h8x/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
```

` nums[i], nums[i0] = nums[i0], nums[i]` ==
```
                tmp = nums[i0]
                nums[i0] = v
                nums[i] = tmp
```

为了保证非零元素的顺序不变，我们需要维护最左边的空位的位置（下标）。
维护 i0 为下界

从左到右遍历 nums[i]。

如果 nums[i]=0，无需交换，只把 i 加一。
