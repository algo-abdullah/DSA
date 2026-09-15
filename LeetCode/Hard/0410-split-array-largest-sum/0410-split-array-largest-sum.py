class Solution(object):
    def count_partitions(self, a, max_sum):
        partitions = 1  # at least one partition
        subarray_sum = 0  # current subarray sum

        for num in a:
            if subarray_sum + num <= max_sum:
                subarray_sum += num
            else:
                partitions += 1
                subarray_sum = num
        return partitions
    def splitArray(self, a, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        low = max(a)  # largest element
        high = sum(a)  # sum of all elements

        # Binary search
        while low <= high:
            mid = (low + high) // 2
            partitions = self.count_partitions(a, mid)

            if partitions > k:
                low = mid + 1  # too many partitions
            else:
                high = mid - 1  # try smaller max_sum
        return low
        