class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        subset = []
        total = 0
        def backtrack(i, subset, total):
            if total == target:
                res.append(subset.copy())
                return
            if i == len(nums) or total > target:
                return    
            subset.append(nums[i])
            backtrack(i, subset, total + nums[i])
            subset.pop()
            backtrack(i + 1, subset, total)
        backtrack(0, [], 0)  
        return res      
                


        