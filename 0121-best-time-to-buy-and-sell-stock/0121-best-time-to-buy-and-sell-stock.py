class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit=0
        buy=prices[0]
        for price in prices:
            buy=min(buy,price) #minPrice는 현재 보고 있는 값의 왼쪽일수 밖에 없음
            profit=max(profit,price-buy)
        return profit