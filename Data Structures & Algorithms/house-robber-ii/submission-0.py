class Solution:
    def rob(self, nums: List[int]) -> int:
        # skip first house, last house
        return max( nums[0], self.helper(nums[1:]), self.helper(nums[:-1]) )
        # edge case, only 1 house

    def helper(self, nums):
        rob1, rob2 = 0, 0
        for n in nums:
            # [rob1, rob2, n - 2, n - 1]
            # rob1 != n - 1
            temp = max(rob1 + n, rob2)
            rob1 = rob2
            rob2 = temp
        
        return rob2
        