from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Inefficient Method
        # buyIndex = 0
        # pastDaysPricesList = []
        # maxProfitTemp = 0

        # for i in range(len(prices)):
        #     for j in range(len(pastDaysPricesList)):
        #         # print(prices[i], pastDaysPricesList[j], maxProfitTemp)
        #         if prices[i] > pastDaysPricesList[j] and prices[i] - pastDaysPricesList[j] > maxProfitTemp:
        #             buyIndex = j
        #             maxProfitTemp = prices[i] - pastDaysPricesList[j]
        #     pastDaysPricesList.append(prices[i])

        # return maxProfitTemp

        if len(prices) < 0:
            return 0

        # Initialize 2 pointers, one to track buying index, and the other to track selling index.
        leftPtr = 0
        rightPtr = 1
        maxProfitTemp = 0

        while rightPtr < len(prices):
            buyPrice = prices[leftPtr]
            sellPrice = prices[rightPtr]
            profit = sellPrice - buyPrice

            # If profit >= 0, check if it is greater than the max profit.
            # If it is, then set it to max profit.
            if profit >= 0:
                if profit > maxProfitTemp:
                    maxProfitTemp = profit
            else:
                # If profit is negative, means a new low was found, so set the new buying index to that.
                leftPtr = rightPtr

            # Increment selling index to always check for the next value.
            rightPtr += 1

        return maxProfitTemp
