class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)

        prefix = [1] * n
        for i in range(1, n):
            prefix[i] = prefix[i - 1] * nums[i - 1]

        postfix = [1] * n
        for j in range(n - 2, -1, -1):
            postfix[j] = postfix[j + 1] * nums[j + 1]

        res = [1] * n
        for k in range(n):
            res[k] = prefix[k] * postfix[k]

        return res
        