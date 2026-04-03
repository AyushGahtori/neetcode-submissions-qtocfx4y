class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1
        
        while l < r:
            # Skip non-alphanumeric characters for left pointer
            while l < r and not ((s[l] >= 'A' and s[l] <= 'Z') or (s[l] >= 'a' and s[l] <= 'z') or (s[l] >= '0' and s[l] <= '9')):
                l += 1
            
            # Skip non-alphanumeric characters for right pointer
            while l < r and not ((s[r] >= 'A' and s[r] <= 'Z') or (s[r] >= 'a' and s[r] <= 'z') or (s[r] >= '0' and s[r] <= '9')):
                r -= 1
            
            # Compare characters (case-insensitive)
            if s[l].lower() != s[r].lower():
                return False
            
            # Move pointers inward
            l += 1
            r -= 1
        
        return True  # If no mismatches are found
