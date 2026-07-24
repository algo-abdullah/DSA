class Solution(object):
    def largestPerimeter(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = sorted(nums)
        nums.reverse()
        for i in range(len(nums)-2):
            if nums[i]<nums[i+1] +nums[i+2]:
                return nums[i]+nums[i+1] +nums[i+2]

        return 0