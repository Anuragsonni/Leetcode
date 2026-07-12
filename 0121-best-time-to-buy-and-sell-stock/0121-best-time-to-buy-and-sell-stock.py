class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        curr_profit=0
        max_profit=0
        invest=prices[0]

        for i in range(len(prices)):
            if prices[i]<= invest:
                invest=prices[i]
            else :
                curr_profit= prices[i]-invest
            if curr_profit> max_profit:
                max_profit= curr_profit
        return max_profit