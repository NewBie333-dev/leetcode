class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # brute force
        n = len(s)
        ans = 0
        for left in range(n):
            s1 = ''
            for right in range(left, n):
                if s[right] in s1:
                    break
                s1 += s[right]
            ans = max(ans, len(s1))
        return ans
