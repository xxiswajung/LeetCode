class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # minPrice = max(prices) # initialise to maximum price
        # maxProfit = 0                
        # for price in prices:
        #     minPrice = min(minPrice, price) # update minimum price to date
        #     maxProfit = max(maxProfit, price - minPrice) # compare with new minimum
        # return maxProfit
    
        left = 0 #Buy
        right = 1 #Sell
        max_profit = 0
        while right < len(prices):
            currentProfit = prices[right] - prices[left] #our current Profit
            if prices[left] < prices[right]:
                max_profit =max(currentProfit,max_profit)
            else:
                left = right
            right += 1
        return max_profit
