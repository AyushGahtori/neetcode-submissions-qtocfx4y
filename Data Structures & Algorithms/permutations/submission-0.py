class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrack(curr):
            if len(curr) == len(nums):
                res.append(curr.copy())   
            for num in nums:
                if num in curr:
                    continue
                curr.append(num)
                backtrack(curr)
                curr.pop()
        backtrack([])  
        return res          

        