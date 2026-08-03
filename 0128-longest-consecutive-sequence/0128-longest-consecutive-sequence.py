class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Step 1: Handle the base case when the list is empty.
        if not nums:
            return 0

        num_set = set(nums)

        cnt = 1           # Initialize a counter for the current consecutive sequence length.
        longest = 1       # Initialize a variable to store the maximum consecutive sequence length.

        # Step 3: Iterate through the elements of 'nums'.
        for num in num_set:
            # Step 4: If the current element 'num' is the start of a sequence (no 'num-1' in 'num_set'),
            if num - 1 not in num_set:
                x = num      # Update 'x' to the current element 'num'.
                cnt = 1
                # Step 5: While consecutive elements exist in 'num_set', increment 'cnt' and 'x'.
                while x + 1 in num_set:
                    cnt += 1
                    x += 1
            
            # Step 6: Update 'longest' with the maximum of 'longest' and 'cnt'.
            longest = max(longest, cnt)

        # Step 7: Return 'longest' as the result.
        return longest
     