# NOTE for future self:
# In Subset II, we can't just remove duplicates from the input array
# because the task requires generating subsets that reflect the original
# count of duplicates. For example, if nums = [1, 2, 2]:
# 
# Input: [1, 2, 2]
# Desired output: [[], [1], [1, 2], [1, 2, 2], [2], [2, 2]]
# 
# If we remove the duplicate 2, the input would become [1, 2], and the
# following subsets would be missed: [2, 2], [1, 2, 2]. 
# 
# Simply removing duplicates results in generated subsets like:
# [[], [1], [2], [1, 2]], which omits valid subsets involving duplicates.
# 
# Therefore, we need to handle duplicates carefully by skipping over them
# at the right time during the backtracking process, ensuring that the
# duplicate subsets are not generated, but all valid unique subsets are.


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = [] #store all the subsets
        nums.sort() # sort the array in nlogn complexity
        store = [] #store the bubsets temperally untill we append it to res 
        def track(i, store):
            if i == len(nums): #when we we visited all the numbers.
                res.append(store.copy())
                return #stops the backtracking

            #do include nums[i]
            store.append(nums[i])
            track(i+1, store)

            #do not include nums[i]
            store.pop()
            #run a while loop to skip all the duplicates in the array.
            #[1, 2, 2] both the condition is gonna run and we skip the second 2
            #point at the end not and i+1 !< len(nums)
            while i + 1 < len(nums) and nums[i] == nums[i+1]:
                i += 1
            track(i+1, store) 
        track(0, []) 
        return res      
            



        