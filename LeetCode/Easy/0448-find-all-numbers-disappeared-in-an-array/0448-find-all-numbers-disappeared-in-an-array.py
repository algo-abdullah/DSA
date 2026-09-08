class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        m = set(nums)
        
        ans = []
        for i in range(1,n+1):
            if i not in m:
                ans.append(i)
        return ans
        