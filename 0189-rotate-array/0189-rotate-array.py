class Solution(object):
    def  d(self,arr,start, end):
        while start < end:
            t = arr[start] 
            arr[start] = arr[end]
            arr[end] = t
            start+=1
            end-=1
    def rotate(self, arr, k):
        # Your code goes here
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(arr)
        k  = k % len(arr)
        self.d(arr,n-k,n-1)
        self.d(arr,0, n-k-1)
        self.d(arr,0, n - 1)
        