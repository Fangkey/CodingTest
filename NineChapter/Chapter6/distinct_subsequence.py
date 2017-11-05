class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        ls = len(s)
        lt = len(t)

        # i for s, row
        # j for t, col
        f = [x[:] for x in [[0] * (lt + 1)] * (ls + 1)]

        for i in range(0, ls):
            f[i][0] = 1

        for i in range(1, ls + 1):
            for j in range(1, lt + 1):
                if s[i - 1] == t[j - 1]:
                    f[i][j] = f[i - 1][j - 1] + f[i - 1][j]
                else:
                    f[i][j] = f[i - 1][j]

        return f[-1][-1]

if __name__ == "__main__":
    s = Solution()

    S = "rabbbit"
    T = "rabbit"
    print s.numDistinct(S, T)
