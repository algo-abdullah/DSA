class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        count = 0
        ps = [0] * n
        ps[0] = nums[0]
        for i in range(1,n):
            ps[i] = ps[i-1]  + nums[i]
        
        m = {}
        for j in range(n):
            if ps[j] == k:
                count+=1
            val = ps[j] - k
            count += m.get(val, 0)
            m[ps[j]]= m.get(ps[j], 0) + 1
        return count
