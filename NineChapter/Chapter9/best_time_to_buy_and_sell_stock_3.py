class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) < 2:
            return 0

        prof_l2r = [0]
        cur_min = prices[0]
        max_prof = 0
        for p in prices[1:]:
            if p - cur_min > max_prof:
                max_prof = p - cur_min
            if p < cur_min:
                cur_min = p
            prof_l2r.append(max_prof)

        prof_r2l = [0]
        cur_max = prices[-1]
        max_prof = 0
        for i in range(len(prices) - 2, -1, -1):
            p = prices[i]
            if p - cur_max < max_prof:
                max_prof = p - cur_max
            if p > cur_max:
                cur_max = p
            prof_r2l.append(-max_prof)

        max_total = 0
        for i in range(0, len(prof_l2r)):
            today = prof_l2r[i] + prof_r2l[len(prof_l2r) - 1 - i]
            if today > max_total:
                max_total = today

        return max_total


if __name__ == "__main__":
    s = Solution()
    prices = [2, 1, 2, 0, 1]
    # 2
    print s.maxProfit(prices)

    prices = [1, 2]
    # 1
    print s.maxProfit(prices)

    prices = [7, 1, 5, 3, 6, 4]
    # 7
    print s.maxProfit(prices)

    prices = [7, 6, 4, 3, 1]
    # 0
    print s.maxProfit(prices)