class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        while l < r:
            while l < r and not((s[l] >= "A" and s[l] <= "z") or (s[l] >= "a" and s[l] <= "z") or (s[l] >= "0" and s[l] <= "9")):
                l += 1
            while l < r and not((s[r] >= "A" and s[r] <= "Z") or (s[r] >= "a" and s[r] <= "z") or (s[r] >= "0" and s[r] <= "9")):
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l+=1
            r-=1    
        return True            

            
         
        