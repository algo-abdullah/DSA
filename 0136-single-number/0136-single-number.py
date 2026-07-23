class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        xor = 0
        for i in range(len(nums)):
            xor ^= nums[i]
        return xor
        