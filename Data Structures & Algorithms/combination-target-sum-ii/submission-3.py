class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        res, i = [], 0
        candidates.sort()

        def backtrack(curr, i, total):
            if total == target:
                res.append(curr.copy())
                return 

            for j in range(i, len(candidates)):
                if j > i and candidates[j] == candidates[j-1]:
                    continue
                if total + candidates[j] > target:
                    break
                curr.append(candidates[j])
                backtrack(curr, j + 1, total + candidates[j])
                curr.pop()
        backtrack([], 0, 0)
        return res        

        