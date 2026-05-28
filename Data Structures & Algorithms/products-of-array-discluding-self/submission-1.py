class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pre, post, res = [0] * n, [0] * n, [0] * n

        pre[0] = post[n - 1] = 1
        for i in range(1, n):
            pre[i] = pre[i - 1] * nums[i - 1]
        
        for j in range(n - 2, -1, -1):
            post[j] = post[j + 1] * nums[j + 1]

        for k in range(n):
            res[k] = pre[k] * post[k]

        return res
            
            
            
        