class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        string = []
        l = 0
        maxs = 0
        for r in range(len(s)):
            while s[r] in string:
                string.remove(s[l])
                l+=1
            string.append(s[r])
            maxs = max(maxs, len(string))
        return maxs       
        