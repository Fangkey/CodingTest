import sys
class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) < 2:
            return 0

        trans_list = []

        buy = False
        buy_price = 0
        for i in range(0, len(prices) - 1):
            if not buy:
                if prices[i + 1] > prices[i]:
                    buy = True
                    buy_price = prices[i]
            else:
                if prices[i + 1] < prices[i]:
                    buy = False
                    trans_list.append((buy_price, prices[i]))

        if buy:
            trans_list.append((buy_price, prices[-1]))

        merge_time = len(trans_list) - k
        for i in range(0, merge_time):
            min_lost = sys.maxint
            merge_index = 0
            is_merge = False
            # important direct delete
            for j in range(0, len(trans_list)):
                if trans_list[j][1] - trans_list[j][0] < min_lost:
                    min_lost = trans_list[j][1] - trans_list[j][0]
                    merge_index = j

            for j in range(0, len(trans_list) - 1):
                trans1 = trans_list[j]
                trans2 = trans_list[j + 1]
                lost = trans1[1] - trans1[0] + trans2[1] - trans2[0] - (trans2[1] - trans1[0])

                if lost < min_lost:
                    min_lost = lost
                    merge_index = j
                    is_merge = True

            merged_trans_list = []
            j = 0
            while j < len(trans_list):
                if merge_index == j:
                    if is_merge:
                        merged_trans_list.append((trans_list[j][0], trans_list[j + 1][1]))
                        j += 1
                else:
                    merged_trans_list.append(trans_list[j])
                j += 1

            trans_list = merged_trans_list

        prof = 0
        for t in trans_list:
            prof += t[1] - t[0]

        return prof


if __name__ == "__main__":
    s = Solution()

    prices = [1, 2, 4, 2, 5, 7, 2, 4, 9, 0]
    # 13
    print s.maxProfit(2, prices)

    prices = [3, 3, 5, 0, 0, 3, 1, 4]
    # 6
    print s.maxProfit(2, prices)

    prices = [1, 2]
    # 1
    print s.maxProfit(1, prices)

    prices = [7, 1, 5, 3, 6, 4]
    # 7
    print s.maxProfit(2, prices)
    # 5
    print s.maxProfit(1, prices)

    prices = [7, 6, 4, 3, 1]
    # 0
    print s.maxProfit(1, prices)
    # 0
    print s.maxProfit(3, prices)

