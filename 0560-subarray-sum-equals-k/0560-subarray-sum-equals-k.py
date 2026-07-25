class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        count = 0
        prefix = 0

        m = {}
        for j in range(n):
            prefix += nums[j]
            if prefix == k:
                count+=1
            val = prefix - k
            count += m.get(val, 0)
            m[prefix]= m.get(prefix, 0) + 1
        return count
