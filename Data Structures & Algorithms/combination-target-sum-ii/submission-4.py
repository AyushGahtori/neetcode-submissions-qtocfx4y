class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []

        def helper(i, total, curr):
            if total == target:
                res.append(curr.copy())
                return

            for j in range(i, len(nums)):
                if total + nums[j] > target:
                    break

                if j > i and nums[j] == nums[j - 1]:
                    continue    

                curr.append(nums[j])
                helper(j + 1, total + nums[j], curr)
                curr.pop()

        helper(0, 0, [])
        return res               
        