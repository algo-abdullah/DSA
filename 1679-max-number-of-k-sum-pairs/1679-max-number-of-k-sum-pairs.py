class Solution(object):
    def maxOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        operations = 0
        nums = sorted(nums)
        i = 0
        j = len(nums)-1
        
        while i < j:
            if nums[i] + nums[j] ==k:
                i+=1
                j-=1
                operations+=1
            elif nums[i] + nums[j] <k:
                i+=1
            else:
                j-=1
        return operations

        