class Solution(object):
    def finalPrices(self, prices):
        """
        :type prices: List[int]
        :rtype: List[int]
        """
        dec = []
        res  = [0] * len(prices)
        for i in range(len(prices)):
            while len(dec) and prices[dec[-1]] >= prices[i]:
                idx = dec.pop()
                res[idx] = prices[i]
            dec.append(i)
        
        return [prices[i] - res[i] for i in range(len(prices))]
        