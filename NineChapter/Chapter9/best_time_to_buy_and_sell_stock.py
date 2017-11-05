class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) == 0:
            return 0

        cur_min = prices[0]
        cur_max_profit = 0

        for n in prices[1:]:
            if n - cur_min > cur_max_profit:
                cur_max_profit = n - cur_min

            if n < cur_min:
                cur_min = n

        return cur_max_profit



if __name__ == "__main__":
    s = Solution()

    prices = [7, 1, 5, 3, 6, 4]
    print s.maxProfit(prices)

    prices = [7, 6, 4, 3, 1]
    print s.maxProfit(prices)