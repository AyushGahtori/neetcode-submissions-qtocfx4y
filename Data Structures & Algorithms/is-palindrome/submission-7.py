class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        while l < r:
            while l < r and not((s[l].lower() >= "a" and s[l].lower() <= "z") or (s[l] >= "0" and s[l] <= "9")):
                l+=1
            while l < r and not((s[r].lower() >= "a" and s[r].lower() <= "z") or (s[r] >= "0" and s[r] <= "9")):
                r-=1
            if s[l].lower() != s[r].lower():
                return False
            l+=1
            r-=1    
        return True               

        