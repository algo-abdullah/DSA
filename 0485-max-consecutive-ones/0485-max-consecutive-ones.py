class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxc = 0
        count = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                count +=1
            else :
                count =0
            if count > maxc:
                maxc = count
        return maxc    