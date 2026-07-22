class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        res =sorted(nums)
        if res[0] != 0:
            return 0

        for i in range(len(nums)-1):
            if res[i] +1!= res[i+1]:
                return res[i]+1
        return len(nums)

        