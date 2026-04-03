class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for n, i in enumerate(nums):
            diff = target - i
            if diff in hashmap:
                return(hashmap[diff], n)
            hashmap[i] = n 


        