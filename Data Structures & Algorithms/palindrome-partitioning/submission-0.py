class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        def backtrack(curr, i):
            # base case: used entire string
            if i == len(s):
                res.append(curr.copy())
                return

            # try all subsrng starting at index 0
            for j in range(i, len(s)):
                sub = s[i:j+1]
                if sub != sub[::-1]:
                    continue
                curr.append(sub)
                backtrack(curr, j + 1)
                curr.pop()
        backtrack([], 0)
        return res