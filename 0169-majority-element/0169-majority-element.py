class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        el = 0
        for i in range(len(nums)):
            if count == 0:
                count+=1
                el = nums[i]
            elif el == nums[i]:
                count+=1
            else:
        
                count-=1
        c = 0

        for j in range(len(nums)):
            if el == nums[j]:
                c+=1
        if c > len(nums)//2:
            return el
        