class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Set and counter to keep track of previous nums + counter
        seen, count = set(nums), 0
        # For loop for num in nums:
        for num in nums:
            if num - 1 not in nums:
                length = 1
                while num + length in seen:
                    # counter ++
                    length += 1
                count = max(count, length)

        # return counter
        return count
        