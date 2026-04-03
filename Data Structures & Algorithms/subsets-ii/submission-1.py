class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = [] #store all the subsets
        nums.sort() # sort the array in nlogn complexity
        store = [] #store the bubsets temperally untill we append it to res 
        def track(i, store):
            if i == len(nums):
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
            



        