import math
class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        low = 1
        high = max(piles)
        while low <= high:
            mid = low +(high - low)//2
            tot= 0
            for i in range(len(piles)):
                tot+=math.ceil(piles[i]/float(mid))
            if tot <= h:
                high = mid -1
            else:
                low = mid + 1
        return low

        