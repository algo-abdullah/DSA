class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals.sort()
        ans = []
        n = len(intervals)
        i = 0
        while i < n:
            start = intervals[i][0]
            end = intervals[i][1]
            j = i + 1
            while j < n and intervals[j][0] <= end:
                end = max(intervals[j][1], end)
                j = j + 1

            ans.append([start,end])
            i = j
        return ans
        