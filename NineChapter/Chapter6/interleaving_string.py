class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        l1 = len(s1)
        l2 = len(s2)
        if len(s3) != (l1 + l2):
            return False

        f = [x[:] for x in [[False] * (l2 + 1)] * (l1 + 1)]
        f[0][0] = True

        for i in range(0, l1 + 1):
            for j in range(0, l2 + 1):
                if i != 0:
                    if s1[i - 1] == s3[i + j - 1]:
                        if f[i - 1][j] == True:
                            f[i][j] = True
                if j != 0:
                    if s2[j - 1] == s3[i + j - 1]:
                        if f[i][j - 1] == True:
                            f[i][j] = True

        return f[-1][-1]



if __name__ == "__main__":
    s = Solution()

    s1 = "aabcc"
    s2 = "dbbca"
    s3 = "aadbbcbcac"
    print s.isInterleave(s1, s2, s3)

    s3 = "aadbbbaccc"
    print s.isInterleave(s1, s2, s3)