class Solution(object):
    def removeOuterParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        ans = ""
        level = 0
        for char in s:
            if char == "(":
                if level > 0:
                    ans+=char
                level+=1
            elif char == ")":
                level-=1
                if level > 0:
                    ans+=char
        return ans       
        