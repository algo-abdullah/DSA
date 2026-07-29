class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxi = -sys.maxsize - 1
        summ  = 0
        for i in range(len (nums)):
            summ+=nums[i]

            if summ > maxi:
                maxi = summ
            
            if summ < 0:
                summ = 0
        return maxi
