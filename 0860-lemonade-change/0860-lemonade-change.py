class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        n = len(bills)
        if n == 0 :
            return false
        count5 = 0
        count10 = 0
        count20 =0
        for i in range(n):
            if bills[i] == 5:
                count5+=1
            elif bills[i] == 10:
                count10+=1
                if count5 != 0:
                    count5-=1
                else:
                    # cant give cahnge
                    return False
            elif bills[i] == 20:
                if count10 != 0 and count5 != 0:
                    count10-=1
                    count5-=1
                elif count5 >= 3:
                    count5 -=3
                else:
                    # //cannot give change  
                    return False
        return True