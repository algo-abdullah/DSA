class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        
        n1 = len(nums1)
        n2 = len(nums2)
        if n1 > n2:
            return self.findMedianSortedArrays(nums2, nums1)
        n = n1+n2
        left = (n1 + n2 + 1) // 2

        low = 0
        high = n1
        while low <= high:
            cut1 = (low+high)//2
            cut2 = left - cut1

            left1 = float('-inf') 
            left2 = float('-inf')  
            right1 = float('inf') 
            right2 = float('inf') 

            if cut1 < n1:
                right1 = nums1[cut1]
            if cut2 < n2:
                right2 = nums2[cut2]
            if cut1 - 1 >= 0:
                left1 = nums1[cut1 - 1]
            if cut2 - 1 >= 0:
                left2 = nums2[cut2 - 1]


            if left1 <= right2 and left2 <= right1:
                # The partition is correct, we found the median
                if n % 2 == 1:
                    return max(left1, left2)
                else:
                    return (max(left1, left2) + min(right1, right2)) / 2.0
            elif left1 > right2:
                # Move towards the left side of nums1
                high = cut1 - 1
            else:
                # Move towards the right side of nums1
                low = cut1 + 1
        
        return 0