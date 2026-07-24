class Solution(object):
    def average(self, salary):
        """
        :type salary: List[int]
        :rtype: float
        """
        mini = min(salary)
        maxi = max(salary)
        sumall = float(0)
        for i in range(len(salary)):
            sumall+=salary[i]
        print(mini, maxi)
        return (sumall-mini-maxi)/(len(salary)-2)
        