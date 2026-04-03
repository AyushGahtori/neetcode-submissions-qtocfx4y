from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        if n == 0 or k == 0:
            return []
        if k == 1:
            return nums[:]   # each element is its own window

        res = []

        # ---- First window: compute max with an O(k) scan ----
        curr_max = nums[0]
        max_idx = 0
        for i in range(1, k):
            if nums[i] > curr_max:
                curr_max = nums[i]
                max_idx = i
        res.append(curr_max)

        # ---- Slide the window ----
        # window is [right-k+1, right] at each step
        for right in range(k, n):
            left = right - k        # index that is leaving the window
            leaving = nums[left]
            new = nums[right]

            if leaving == curr_max:
                # The current maximum is leaving the window
                if new > curr_max:
                    # New element becomes the new max
                    curr_max = new
                    max_idx = right
                else:
                    # Need to recompute max in the new window [left+1 .. right]
                    start = left + 1
                    curr_max = nums[start]
                    max_idx = start
                    for i in range(start + 1, right + 1):
                        if nums[i] > curr_max:
                            curr_max = nums[i]
                            max_idx = i
            else:
                # The current maximum is still in the window
                if new > curr_max:
                    curr_max = new
                    max_idx = right

            res.append(curr_max)

        return res
