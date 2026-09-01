class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        low = 0
        
        high = len(nums) - 1
        ans = float("inf")

        while low <= high:
            mid = low + (high - low )//2
            if nums[low] <= nums[mid]:
                ans = min(nums[low],ans)
                low = mid + 1
            else:
                ans = min(ans, nums[mid])
                high = mid - 1
        return ans
        