class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        m1 = {}
        m2 = {}
        for i in s:
            m1[i] = m1.get(i,0)+1
        for i in t:
            m2[i] = m2.get(i,0)+1
        return m1 == m2

        