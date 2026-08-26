class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        pre , suff = 1 ,1 
        ans = float('-inf')
        n = len(nums)
        for i in range(len(nums)):
            if pre == 0:
                pre = 1
            if suff == 0:
                suff = 1
            pre *= nums[i]
            suff *= nums[n - i - 1]
            ans = max(ans, pre , suff)
        return ans
        