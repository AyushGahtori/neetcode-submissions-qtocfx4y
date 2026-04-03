class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        cur = []
        def dfs(i, total, cur): #I because in this solution we will use one value only once
            if total == target:
                res.append(cur.copy())
                return 
            if i>=len(nums) or total > target:
                return
            #decides to add.    
            cur.append(nums[i]) #chose to include
            #i stays the same because potentially we can include the same number again
            #we pass cur because we just updated it.
            #we pass total because it did endup changing.
            dfs(i, total + nums[i], cur)
            #decides not to add
            cur.pop() #chose not to include
            #i+1 because we cannot include i now.
            #total stays the same because we didn't chose to add.
            dfs(i + 1, total, cur)
        dfs(0, 0, [])
        return res    




    