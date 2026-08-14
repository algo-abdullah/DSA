class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        i = len(s) -1
        res = ""
        word = ''
        while i>=0:
            while i>=0 and s[i]==" ":
                i-=1
            if i<0:
                break
            end =i 
            while i>=0 and s[i] != " ":
                i-=1
            word = s[i+1:end+1]
            if res != "":
                res+=" "
            res+=word
        return res
        