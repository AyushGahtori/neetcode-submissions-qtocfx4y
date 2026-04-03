class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        for num in nums:
            new_subsets = []
            for subset in res:
                new_subsets.append(subset + [num])
            res.extend(new_subsets)
        return res
