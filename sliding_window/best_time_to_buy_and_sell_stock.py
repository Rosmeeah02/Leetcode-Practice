""" Notes: 
-> float('inf') -> infinity(very big #) -> so that the first value replaces it
-> min (a,b) -> smaller of 2 values -> helps track smallest price
-> Use short names (i, j) for indexes,
-> Use clear names (price, num, char) for real data. """

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        max_profit = 0

        for price in prices[1:]:
            profit = price - min_price
            max_profit = max(max_profit, profit)

            if price < min_price:
                min_price = price

        return max_profit  

#Difficulty: Easy
#Time Complexity: O(n)
#Space Complexity: O(1)
