class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        l1 = len(word1)
        l2 = len(word2)

        f = [x[:] for x in [[0] * (l2 + 1)] * (l1 + 1)]

        for i in range(0, l1 + 1):
            f[i][0] = i
        for j in range(0, l2 + 1):
            f[0][j] = j

        for i in range(1, l1 + 1):
            for j in range(1, l2 + 1):
                if word1[i - 1] == word2[j - 1]:
                    # This line is from video , but it can not be explained
                    #f[i][j] = min(f[i - 1][j - 1], f[i][j - 1] + 1, f[i - 1][j] + 1)

                    # This line is OK for Leetcode
                    f[i][j] = f[i - 1][j - 1]
                else:
                    f[i][j] = min(f[i - 1][j - 1] + 1, f[i][j - 1] + 1, f[i - 1][j] + 1)

        return f[l1][l2]




if __name__ == "__main__":
    s = Solution()

    A = "mart"
    B = "karma"
    print s.minDistance(A, B)

    A = "www.lintcode.com code"
    B = "www.ninechapter.com code"
    print s.minDistance(A, B)