class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) < 2:
            return 0

        prof = 0
        buy = False
        buy_p = 0
        for i in range(0, len(prices) - 1):
            if buy == False:
                if prices[i + 1] - prices[i] > 0:
                    buy_p = prices[i]
                    buy = True
            else:
                if prices[i + 1] - prices[i] < 0:
                    prof += prices[i] - buy_p
                    buy = False

        if buy == True:
            prof += prices[-1] - buy_p

        return prof


if __name__ == "__main__":
    s = Solution()
    prices = [1, 2]
    print s.maxProfit(prices)

    prices = [7, 1, 5, 3, 6, 4]
    print s.maxProfit(prices)

    prices = [7, 6, 4, 3, 1]
    print s.maxProfit(prices)