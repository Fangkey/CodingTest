class Solution1:
    """
    @param: m: An integer m denotes the size of a backpack
    @param: A: Given n items with size A[i]
    @param: V: Given n items with value V[i]
    @return: The maximum value
    """
    def backPackII(self, m, A, V):
        # write your code here
        f = [x[:] for x in [[0] * (m +1)] * (len(A) + 1)]

        for i in range(1, len(A) + 1):
            for j in range(0, m + 1):
                if j + A[i - 1] <= m:
                    if f[i - 1][j] + V[i - 1] > f[i][j + A[i - 1]]:
                        for k in range(i, len(A) + 1):
                            f[k][j + A[i - 1]] = f[i - 1][j] + V[i - 1]

        return f[-1][-1]


class Solution:
    def backPackII(self, m, A, V):
        # Max Value for items <= i and sum(m) <= j
        f = [x[:] for x in [[0] * (m + 1)] * (len(A) + 1)]
        for i in range(1, len(A) + 1):
            for j in range(0, m + 1):
                if j - A[i - 1] >= 0:
                    if f[i][j] < f[i - 1][j - A[i - 1]] + V[i - 1]:
                        f[i][j] = f[i - 1][j - A[i - 1]] + V[i - 1]
                else:
                    f[i][j] = f[i - 1][j]

        return f[-1][-1]


if __name__ == "__main__":
    s = Solution()

    A = [3, 3, 5, 6]
    V = [1, 5, 2, 4]
    m = 10
    # 9
    print s.backPackII(m, A, V)

    A = [2, 3, 5, 7]
    V = [1, 5, 2, 4]
    m = 10
    # 9
    print s.backPackII(m, A, V)