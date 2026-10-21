class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest, lookup = 0, set(nums)
        for num in nums:
            if num - 1 not in lookup:
                length = 0
                while num + length in lookup:
                    length += 1

                longest = max(longest, length)

        return longest

