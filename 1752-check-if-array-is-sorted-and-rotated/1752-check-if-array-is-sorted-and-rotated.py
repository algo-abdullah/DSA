class Solution(object):
    def check(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        count = 0
        n =  len(nums)
        for i in range(1,n):
            if nums[i] < nums[i-1]:
                count+=1
            
        if nums[n-1] > nums[0]:
            count+=1
        if count <= 1:
            return True
        else:
            return False