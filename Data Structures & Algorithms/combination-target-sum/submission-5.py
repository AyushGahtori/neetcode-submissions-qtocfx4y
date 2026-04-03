class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()
        def helper(i, curr, total):
            if total == target and curr not in res:
                res.append(curr.copy())
                return
            if total > target:
                return

            for j in range(i, len(nums)):
                curr.append(nums[j])
                helper(j, curr, total + nums[j])
                curr.pop()

        helper(0, [], 0) 
        return res            
        