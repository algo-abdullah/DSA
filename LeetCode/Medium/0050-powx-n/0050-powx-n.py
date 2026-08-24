      
class Solution:
    """
        :type x: float
        :type n: int
        :rtype: float
        """
    def myPow(self, x, n):
        p = 1.00
        k = n

        if n < 0:
            x = 1 / x
            k = -k

        while k > 0:
            if k % 2 == 1:
                p = p * x

            x = x * x
            k = k // 2

        return p        