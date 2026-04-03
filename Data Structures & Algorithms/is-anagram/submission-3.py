class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_hash, t_hash = {}, {}

        for i in range(len(s)):
            s_hash[s[i]] = 1 + s_hash.get(s[i], 0) 

        for i in range(len(t)):
            t_hash[t[i]] = 1 + t_hash.get(t[i], 0)

        return s_hash == t_hash    
        