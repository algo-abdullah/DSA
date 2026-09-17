class Solution(object):
    def buildArray(self, target, n):
        """
        :type target: List[int]
        :type n: int
        :rtype: List[str]
        """
        res= []
        c = 0 
        for i in range(1,n+1):
            res.append("Push")
            if target[c]!= i :
                res.append("Pop")
            else:
                c+=1
            i+=1
            if c>=len(target):
                break
        return res