class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0 # 최대 이익
        min_price = prices[0] # 최소 가격

        for price in prices:
            # 최소 가격 갱신
            if price < min_price:
                min_price = price
                continue
            
            # 최대 이익 갱신
            if max_profit < price - min_price:
                max_profit = price - min_price
        
        return max_profit
