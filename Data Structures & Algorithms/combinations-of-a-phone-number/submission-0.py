class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        res = []
        digittochar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        #curr = current string
        def backtrack(i, curr): # # i = what index we are in the digit(input) string
            if len(curr) == len(digits):
                res.append(curr)
                return
            for c in digittochar[digits[i]]: #every character in this string for example i = 2 for c in abc
                backtrack(i + 1, curr + c)      
        backtrack(0, "") #curr string is empty at bigening
        return res




        