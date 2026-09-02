class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """

        
        m = {}
        for i  in range(len(t)):
            
            m[t[i]] = m.get(t[i] , 0) +1
        for i in range(len(s)):
            m[s[i]] -= 1
            if m[s[i]] == 0:
                del m[s[i]]
        return list(m.keys())[0]
        