### 暴力算法
nested loop 遍历

### 双指针
前面的暴力算法没有用到sorted这个条件，这里要求常量级的时间复杂度，所以不能用hashtable.
`Your solution must use only constant extra space.`

维护一个left，一个right
当nums[left] + nums[right] > target 时说明：right和[left, right]中间所有的数相加都大于target，所以可以排除right，即right -= 1

当nums[left] + nums[right] < target 时说明：left和[left, right]中间所有的数相加都小于target，所以可以排除left，即left += 1

结束条件：left < right



https://leetcode.cn/problems/two-sum-ii-input-array-is-sorted/solutions/1968341/san-shu-zhi-he-bu-hui-xie-xiang-xiang-sh-6wbq/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处
