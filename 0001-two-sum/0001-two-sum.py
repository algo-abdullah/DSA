class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        numMap = {}
        for i,n in enumerate(nums):
            diff = target - n
            if diff in numMap:
                return [numMap[diff],i]
            numMap[n]= i
        return 
             