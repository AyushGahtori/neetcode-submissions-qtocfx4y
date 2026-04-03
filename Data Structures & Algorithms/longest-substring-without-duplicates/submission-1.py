class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substr = []
        l = 0
        res = 0
        for r in range(len(s)):
            while s[r] in substr:
                substr.remove(s[l])
                l += 1
            substr.append(s[r])
            res = max(res, r - l + 1)
        return res        
        