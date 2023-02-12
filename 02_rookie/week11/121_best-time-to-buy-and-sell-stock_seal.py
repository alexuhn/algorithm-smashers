class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        bottom = prices[0]
        biggest = 0

        i = 1
        while (i < len(prices)):
            biggest = max(biggest, prices[i] - bottom)
            bottom = min(bottom, prices[i])

            i += 1

        return biggest


# second try
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        bottom = prices[0]
        biggest = 0

        i = 1
        while (i < len(prices)):
            if biggest < prices[i] - bottom:
                biggest = prices[i] - bottom 
            if bottom > prices[i]:
                bottom = prices[i] 
            i += 1

        return biggest