class Solution(object):
    def applyOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        for i in range(n-1):
            if nums[i] == nums[i + 1]:
                nums[i] = nums[i]*2
                nums[i+1] = 0
        j = 0
        for i in range(n):
            if nums[i] != 0:
                nums[i] , nums[j] = nums[j] , nums[i]
                j+=1
        return nums