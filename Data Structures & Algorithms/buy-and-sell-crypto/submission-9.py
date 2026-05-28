class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, most = 0, 0
        for r in range(1, len(prices)):
            if prices[r] > prices[l]:
                most = max(most, prices[r] - prices[l])
            else:
                l = r

        return most

        