[官方题解（看滑动窗口的动画）](https://leetcode.cn/problems/minimum-size-subarray-sum/solutions/305704/chang-du-zui-xiao-de-zi-shu-zu-by-leetcode-solutio/)
```
class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        if not nums:
            return 0
        
        n = len(nums)
        ans = n + 1
        start, end = 0, 0
        total = 0
        while end < n:
            total += nums[end]
            while total >= s:
                ans = min(ans, end - start + 1)
                total -= nums[start]
                start += 1
            end += 1
        
        return 0 if ans == n + 1 else ans

作者：力扣官方题解
链接：https://leetcode.cn/problems/minimum-size-subarray-sum/solutions/305704/chang-du-zui-xiao-de-zi-shu-zu-by-leetcode-solutio/
来源：力扣（LeetCode)
```

2.使用队列相加（实际上我们也可以把它称作是滑动窗口，这里的队列其实就相当于一个窗口）

我们把数组中的元素不停的入队，直到总和大于等于 s 为止，接着记录下队列中元素的个数，然后再不停的出队，直到队列中元素的和小于 s 为止（如果不小于 s，也要记录下队列中元素的个数，这个个数其实就是不小于 s 的连续子数组长度，我们要记录最小的即可）。接着再把数组中的元素添加到队列中……重复上面的操作，直到数组中的元素全部使用完为止。
这里以 [2,3,1,2,4,3] 举例画个图来看下

作者：数据结构和算法
**看图**
链接：https://leetcode.cn/problems/minimum-size-subarray-sum/solutions/306066/javade-jie-fa-ji-bai-liao-9985de-yong-hu-by-sdwwld/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
```
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        right, left = 0, 0
        n = len(nums)
        total = 0
        ans = n + 1
        while right < n:
            total += nums[right]
            while total >= target:
                ans = min(ans, right-left+1)
                total -= nums[left]
                left += 1
            right += 1
        return ans if ans != n + 1 else 0
```
这种方法完全对应了上面的queue的图
