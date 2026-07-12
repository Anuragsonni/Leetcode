class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit=0
        invest=prices[0]

        for prise in prices:
            if prise <= invest:
                invest=prise
            elif prise-invest> max_profit:
                max_profit = prise -invest
        return max_profit