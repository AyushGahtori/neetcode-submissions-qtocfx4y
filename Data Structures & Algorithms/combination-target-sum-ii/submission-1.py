#to better understand this problem do these questions:
#combination sum
#subset 2


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = [] # to store the result at the end
        store = [] # to store the candidates[i] as we use recursion
        candidates.sort() #important to skip the same numbers
        def sum(i, store, total):
            if total == target: #if we sound a valid combination sum
                res.append(store.copy())
                return #stop the backtracking
            if i >= len(candidates) or total > target:
                return #stop the backtracking

            store.append(candidates[i]) #chose to include
            sum(i+1, store, total + candidates[i])
            store.pop() #chose not to include

            #run a while loop to skip all the duplicates in the array.
            #[1, 2, 2] both the condition is gonna run and we skip the second 2
            #point at the end not and i+1 !< len(nums)            
            while i + 1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1 #skip over the same numbers
            sum(i+1, store, total)

        sum(0, [], 0) 
        return res #return the res at the end          

                    