class Solution:
    """
    @param: A: A string
    @param: B: A string
    @return: the length of the longest common substring.
    """
    def longestCommonSubstring(self, A, B):
        # write your code here
        la = len(A)
        lb = len(B)

        f = [x[:] for x in [[0] * (lb + 1)] * (la + 1)]

        for i in range(0, la):
            for j in range(0, lb):
                if A[i] == B[j]:
                    f[i + 1][j + 1] = f[i][j] + 1
                else:
                    f[i + 1][j + 1] = 0

        return max([max(l) for l in f])


if __name__ == "__main__":
    s = Solution()

    A = "www.lintcode.com code"
    B = "www.ninechapter.com code"
    print s.longestCommonSubstring(A, B)

    A = "ABCD"
    B = "EDCA"
    # 1
    print s.longestCommonSubstring(A, B)

    A = "ABCD"
    B = "EACB"
    # 1
    print s.longestCommonSubstring(A, B)


    A = "ABCD"
    B = "CBCE"
    # 3
    print s.longestCommonSubstring(A, B)