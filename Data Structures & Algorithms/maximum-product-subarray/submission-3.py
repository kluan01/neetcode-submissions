class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)

        dp_max, dp_min = [0] * n, [0] * n
        dp_max[0], dp_min[0] = nums[0], nums[0] # base case

        # Transition: at each i, the best subarray ending here is either
        #   (a) nums[i] alone (start fresh), or
        #   (b) nums[i] extending the previous best max, or
        #   (c) nums[i] extending the previous best min (matters when nums[i] < 0)
        for i in range(1, n):
            candidates = [
                nums[i],
                nums[i] * dp_max[i - 1],
                nums[i] * dp_min[i - 1],
            ]

            dp_max[i] = max(candidates)
            dp_min[i] = min(candidates)

        return max(dp_max)


        