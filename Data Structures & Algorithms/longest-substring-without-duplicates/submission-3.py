class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        rset = set()
        l = 0
        res = 0
        for r in range(len(s)):
            while s[r] in rset:
                rset.remove(s[l])
                l += 1
            rset.add(s[r])
            res = max(res, r - l + 1)
        return res    

        