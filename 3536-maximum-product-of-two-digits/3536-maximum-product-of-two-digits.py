class Solution(object):
    def maxProduct(self, n):
        """
        :type n: int
        :rtype: int
        """
        t = n
        dig = 0
        prod = 0
        prev = 1
        while t:
            dig = t %10
            nex = t/10
            while nex:
                sdig = nex%10
                prev = sdig * dig 
                if  prev > prod:
                    prod = prev
                nex/=10
            t = t/10
        return prod
        