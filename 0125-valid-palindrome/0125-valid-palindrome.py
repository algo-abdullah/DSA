class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        ans = str()
        for i in range(len(s)):
            if s[i].isalnum():
                ans+=s[i].lower()
        print(ans)
        i,j = 0, len(ans)-1
        while i < j:
            if ans[i]!=ans[j]:
                return False
            j-=1
            i+=1

        return True
        