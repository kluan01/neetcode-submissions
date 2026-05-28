class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Set and counter to keep track of previous nums + counter
        seen, count = set(nums), 0
        # For loop for num in nums:
        for num in nums:
            # If val - 1 is in seen:
            curr = num
            counter = 1
            while curr - 1 in seen:
                # counter ++
                counter += 1
                curr -= 1
            count = max(count, counter)

        # return counter
        return count
        