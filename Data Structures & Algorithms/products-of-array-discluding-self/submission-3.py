class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n

        prefix = 1
        for i in range(n):              # walk 1: left to right
            res[i] = prefix             # write first: product of everything left of i
            prefix *= nums[i]           # then multiply nums[i] in

        postfix = 1
        for i in range(n - 1, -1, -1):  # walk 2: right to left
            res[i] *= postfix           # write first: times everything right of i
            postfix *= nums[i]          # then multiply nums[i] in

        return res