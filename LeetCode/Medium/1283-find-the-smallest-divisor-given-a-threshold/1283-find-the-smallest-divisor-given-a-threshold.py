import math
class Solution(object):
    def sumByD(self, arr, div):
        return sum(math.ceil(x / float(div)) for x in arr)

    def smallestDivisor(self, nums, threshold):
        """
        :type nums: List[int]
        :type threshold: int
        :rtype: int
        """
        if len(nums) > threshold:
            return -1
        low = 1
        high = max(nums)
        while low <= high:
            mid = low +(high - low )//2
            if self.sumByD(nums, mid) <= threshold:
                high = mid -1
            else:
                low = mid +1
        return low


        