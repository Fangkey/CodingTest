class Solution:
    """
    @param: A: An integer array
    @param: target: An integer
    @return: An integer
    """
    def MinAdjustmentCost(self, A, target):
        # write your code here
        f = [x[:] for x in [[0] * 101] * (len(A) + 1)]

        for j in range(1, 101):
            f[1][j] = abs(A[0] - j)

        for i in range(2, (len(A) + 1)):
            for j in range(1, 101):
                low = max(1, j - target)
                high = min(100, j + target)
                cand = []
                for k in range(low, high + 1):
                    cand.append(f[i - 1][k] + abs(A[i - 1] - j))
                f[i][j] = min(cand)

        return min(f[-1][1:])


if __name__ == "__main__":
    s = Solution()

    A = [1, 4, 2, 3]
    target = 1
    # 2
    print s.MinAdjustmentCost(A, target)