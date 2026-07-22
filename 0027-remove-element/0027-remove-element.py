class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        k = 0 
        j = len(nums) -1
        i=0
        while i <=j:
            if  nums[i] != val:
                k+=1
            if nums[i] == val:
                nums[i] = nums[j]
                j = j-1 
            else: i+=1
        return k   
      