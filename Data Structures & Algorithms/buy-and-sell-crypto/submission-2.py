class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2: return 0

        l, r = 0, 1
        most = 0
        for r in range(len(prices)):
            if prices[r] > prices[l]:
                most = max(most, prices[r] - prices[l])
            else:
                l = r

            r += 1
        return most
                



        