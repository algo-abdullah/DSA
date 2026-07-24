class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        N = len(nums)
        i = 0
        j = n
        k = 0
        ans = [0]* N
        while k < N  :
            if k % 2 == 0:
                ans[k] = nums[i]
                i+=1
            else:
                ans[k] = nums[j]
                j+=1
            
            k+=1
            
           
        return ans