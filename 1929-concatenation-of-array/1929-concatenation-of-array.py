class Solution(object):
    def getConcatenation(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        i=0
        j=0
        ans = [0]*len(nums*2)
        while i< len(nums*2):
            if i <len(nums):
                ans[i] = nums[i]
                i+=1
                
            else:
                ans[i] = nums[j]
                j+=1
                i+=1

        return ans