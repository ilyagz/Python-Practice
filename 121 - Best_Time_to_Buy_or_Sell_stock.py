/* 
121. Best Time to Buy and Sell Stock

Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Note that you cannot sell a stock before you buy one.
*/

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        maxprofit = 0
        for i in range(0,len(prices)-1):
            for j in range (i+1, len(prices)):
                profit = prices[j] - prices[i]
                if (profit > maxprofit):
                    maxprofit = profit
        return maxprofit