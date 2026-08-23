class Solution(object):
    def reverse(self, x):
        sign = -1 if x < 0 else 1
        x = abs(x)

        rev = 0

        while x != 0:
            dig = x % 10
            x //= 10
            rev = rev * 10 + dig

        rev *= sign

        if rev < -2147483648 or rev > 2147483647:
            return 0

        return rev