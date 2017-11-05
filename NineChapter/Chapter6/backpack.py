class Solution1:
    # @param m: An integer m denotes the size of a backpack
    # @param A: Given n items with size A[i]
    # @return: The maximum size
    def backPack(self, m, A):
        f = [x[:] for x in [[False] * (m + 1)] * (len(A) + 1)]
        # i for items
        # j for size

        for i in range(0, len(A) + 1):
            f[i][0] = True

        for i in range(1, len(A) + 1):
            for j in range(0, m + 1):
                # important
                if f[i - 1][j] == True:
                    f[i][j] = f[i - 1][j]
                if f[i - 1][j] == True and j + A[i - 1] <= m:
                    f[i][j + A[i - 1]] = True

        for j in range(m, -1, -1):
            for i in range(len(A), -1, -1):
                if f[i][j]:
                    return j


class Solution:
    def backPack(self, m, A):
        # can make: mass=j and items <= i
        f = [x[:] for x in [[False] * (m + 1)] * (len(A) + 1)]

        # init
        for i in range(0, len(A) + 1):
            f[i][0] = True

        # Transfer
        for i in range(1, len(A) + 1):
            for j in range(0, m + 1):
                if j < A[i - 1]:
                    f[i][j] = f[i - 1][j]
                else:
                    if f[i - 1][j - A[i - 1]]:
                        f[i][j] = True

        for j in range(m, -1, -1):
            for i in range(len(A), -1, -1):
                if f[i][j]:
                    return j

if __name__ == "__main__":
    s = Solution()

    A = [3, 4, 8, 5]
    m = 10
    # 9
    print s.backPack(m, A)

    A = [2, 3, 5, 7]
    m = 11
    # 10
    print s.backPack(m, A)

    A = [2, 3, 5, 7]
    m = 12
    # 12
    print s.backPack(m, A)