class Solution:
    """
    @param: A: An integer array
    @param: k: A positive integer (k <= length(A))
    @param: target: An integer
    @return: An integer
    """
    def kSum(self, A, k, target):
        # write your code here
        f = []
        for i in range(0, len(A) + 1):
            f.append([x[:] for x in [[0] * (target + 1)] * (k + 1)])

        for i in range(0, len(A) + 1):
            f[i][0][0] = 1

        for i in range(1, len(A) + 1):
            for j in range(1, k + 1):
                for t in range(0, target + 1):
                    # important, can improve speed.
                    # assign all rest i like this is slow:
                    # if t >= A[i - 1]:
                    #     for n in range(i, len(A) + 1):
                    #         f[n][j][t] = f[i - 1][j - 1][t - A[i - 1]]
                    if t >= A[i - 1]:
                        f[i][j][t] = f[i - 1][j - 1][t - A[i - 1]]
                    f[i][j][t] += f[i - 1][j][t]

        return f[len(A)][k][target]


if __name__ == "__main__":
    s = Solution()

    A = [1, 2, 3, 4]
    k = 2
    target = 5
    # 2
    print s.kSum(A, k, target)