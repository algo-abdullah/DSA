class Solution(object):
    def daysNeeded(self, weights, capacity):
        # Initialize count of days to 1
        days = 1
        # Initialize current load on ship to 0
        currentLoad = 0


        # Iterate over all package weights
        for w in weights:
            # Check if adding current package exceeds capacity
            if currentLoad + w > capacity:
                # If yes, increase days count since we start a new day
                days += 1
                # Reset current load to current package weight
                currentLoad = w
            else:
                # Else, add current package weight to current load
                currentLoad += w
        # Return total days required
        return days

        
    def shipWithinDays(self, weights, days):
        """
        :type weights: List[int]
        :type days: int
        :rtype: int
        """
        left = max(weights)
        # Calculate maximum capacity as sum of all weights
        right = sum(weights)

        # Binary search between left and right capacity values
        while left < right:
            # Calculate mid value to test
            mid = left + (right - left) // 2
            # Calculate how many days needed for capacity mid
            needed = self.daysNeeded(weights, mid)

            # If days needed is less or equal to allowed days,
            # try to find smaller capacity on left side
            if needed <= days:
                right = mid
            else:
                # Else, need more capacity, search on right side
                left = mid + 1

        # Return minimum capacity found
        return left
         