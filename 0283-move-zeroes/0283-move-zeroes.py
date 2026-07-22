class Solution(object):
    def moveZeroes(self, arr):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        j = -1
    	n = len (arr)
    	for i in range(n):
    	    if arr[i ]  == 0:
    	        j = i 
    	        break
    	if j == -1:
    	    return
    	
    	for i in range(j+1, n):
    	    if arr[i] != 0:
    	        t = arr[i]
    	        arr[i] = arr[j]
    	        arr[j] = t
    	        j+=1
        