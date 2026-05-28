class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2: return 0

        l, most = 0, 0
        for r in range(1, len(prices)):
            if prices[r] > prices[l]:
                most = max(most, prices[r] - prices[l])
            else:
                l = r

            r += 1
        return most

        