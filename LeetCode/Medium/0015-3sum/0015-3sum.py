class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        ans = []
        n = len(nums)
        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:continue
            j = i + 1
            k = n - 1
            while j < k:
                tar = nums[i] + nums[j] + nums[k]
                if tar < 0:
                    j+=1
                elif tar > 0:
                    k-=1
                else:
                    temp = [nums[i],nums[j],nums[k]]
                    ans.append(temp)
                    j+=1
                    k-=1
                    while(j < k and nums[j] == nums[j-1]):j+=1
                    while(j < k and nums[k] == nums[k+1]):k-=1

            
        return ans