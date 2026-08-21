class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        ans = set()
        n = len(nums)
        for i in range(n):
            for j in range(i+1,n):
                hashset = set()
                for k in range(j+1,n):
                    fourth = target - nums[i] - nums[j] -nums[k]
                    if fourth in hashset:
                        t = tuple(sorted([nums[i],nums[j],nums[k],fourth]))
                        
                        ans.add(t)
                    hashset.add(nums[k])
        return [list(t) for t in ans]