class Solution(object):
    def occurrencesOfElement(self, nums, queries, x):
        """
        :type nums: List[int]
        :type queries: List[int]
        :type x: int
        :rtype: List[int]
        """
        indices = [i for i, val in enumerate(nums) if val == x]
        ans = []
        for q in queries:
            if q <= len(indices):
                ans.append(indices[q-1])
            else:
                ans.append(-1)
        return ans

        