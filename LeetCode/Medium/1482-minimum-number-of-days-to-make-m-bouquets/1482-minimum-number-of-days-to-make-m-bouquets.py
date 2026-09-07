class Solution(object):
    def canbloom(self,arr,day,m,k):
        cnt = 0
        bouquets = 0
        for i in range(len(arr)):
            if arr[i] <= day:
                cnt+=1
                if cnt == k:
                    bouquets += 1
                    cnt = 0
            else:
                
                cnt = 0
        if bouquets >= m:
            return True
        else:
            return False

    def minDays(self, bloomDay, m, k):
        """
        :type bloomDay: List[int]
        :type m: int
        :type k: int
        :rtype: int
        """
        if m * k > len(bloomDay):
            return -1 
        maxi = max(bloomDay)
        mini = min(bloomDay)
        low = mini
        high = maxi
        ans = -1
        while low <= high:
            mid = low + (high- low)//2
            val = self.canbloom(bloomDay,mid,m,k)
            if val == True:
                ans = mid
                high = mid - 1
            else:
                low = mid +1 
        return ans