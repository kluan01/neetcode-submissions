class Solution:
    def findMin(self, nums: List[int]) -> int:
        # bin search
        l, r = 0, len(nums) - 1
        # min count
        best = nums[0]

        while l <= r:
            # check if left val < right val
                # true? min = left
            if nums[l] < nums[r]:
                best = min(best, nums[l])
                break

            # find m value
            m = l + (r - l) // 2
            # check min val since we are using inclusion
            best = min(best, nums[m])

            # if m val > l val:
            if nums[m] >= nums[l]:
                l = m + 1
                # move l val
            else:
                r = m - 1
                # move r val

        return best
            
        