class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # for num in nums
        # if len(curr) == len(nums)
        # if nums in curr: continue

        res = []

        def helper(curr):
            if len(curr) == len(nums):
                res.append(curr.copy())
                return

            for num in nums:
                if num in curr:
                    continue
                curr.append(num) 
                helper(curr)
                curr.pop() 
        helper([]) 
        return res             
        