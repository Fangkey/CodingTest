# coding=utf-8

# 2018-05-10 22:52
# 2018-05-10 22:02

class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """

        a = [0] * (len(cost) + 1)
        a[0] = 0
        a[1] = cost[0]

        for i in range(2, len(cost) + 1):
            if a[i - 2] > a[i - 1]:
                a[i] = a[i - 1] + cost[i - 1]
            else:
                a[i] = a[i - 2] + cost[i - 1]

        return min(a[-2], a[-1])


if __name__ == "__main__":
    s = Solution()

    cost = [0, 0, 0, 1]
    # 0
    print s.minCostClimbingStairs(cost)

    cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
    # 6
    print s.minCostClimbingStairs(cost)

