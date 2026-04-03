class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low, high = 1, max(piles)
        res = high

        def check(mid):
            total_time = 0
            for pile in piles:
                total_time += math.ceil(pile / mid)
            return total_time <= h

        while low <= high:
            mid = (low + high) // 2
            if (check(mid)):
                res = mid
                high = mid - 1
            else:
                low = mid + 1
        return res