class Solution(object):
    def exclusiveTime(self, n, logs):
        """
        :type n: int
        :type logs: List[str]
        :rtype: List[int]
        """
        stack = []
        result = [0]*n
        def parselog(processtime):
            return processtime.encode('ascii','igonre').split(':')
        
        for ps in logs:
            psId , eventType , time = parselog(ps)

            if eventType== "start":
                stack.append([psId,time])
            elif eventType == 'end':
                psId , startTime=stack.pop()
                timeSpent = int(time)- int(startTime)+1
                result[int(psId)] += timeSpent

                if len(stack) != 0:
                    nextPsId , timeSpentbyNextProcess = stack[-1]
                    result[int(nextPsId)] -= timeSpent
        return result