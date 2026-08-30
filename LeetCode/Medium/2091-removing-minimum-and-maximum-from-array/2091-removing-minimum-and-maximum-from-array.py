class Solution(object):
    def minimumDeletions(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        mn = 0
        mx = 0
        for i in range(1,len(nums)):
            if nums[mn] < nums[i]:
                mn = i
            if nums[mx] > nums[i]:
                mx = i
        n = len(nums) 
        left = min(mn, mx)
        right = max(mn, mx)
       # Option 1: Remove both from the left
        option1 = right + 1

        # Option 2: Remove both from the right
        option2 = n - left

        # Option 3: Remove min from left and max from right
        option3 = (left + 1) + (n - right)

        return min(option1, option2, option3)