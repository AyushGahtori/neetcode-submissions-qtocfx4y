class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        store = []
        candidates.sort() 
        def sum(i, store, total):
            if total == target:
                res.append(store.copy())
                return
            if i >= len(candidates) or total > target:
                return 

            store.append(candidates[i])
            sum(i+1, store, total + candidates[i])
            store.pop()
            while i + 1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1
            sum(i+1, store, total)
        sum(0, [], 0) 
        return res           

                    