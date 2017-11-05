class Solution:
    """
    @param A, B: Two strings.
    @return: The length of longest common subsequence of A and B.
    """
    def longestCommonSubsequence(self, A, B):
        la = len(A)
        lb = len(B)
        f = [x[:] for x in [[0] * (la + 1)] * (lb + 1)]

        for i in range(0, la):
            for j in range(0, lb):
                if A[i] == B[j]:
                    f[i + 1][j + 1] = f[i][j] + 1
                else:
                    f[i + 1][j + 1] = max([f[i][j + 1], f[i + 1][j]])

        return f[la][lb]





if __name__ == "__main__":
    s = Solution()

    A = "ABCD"
    B = "EDCA"
    # 1
    print s.longestCommonSubsequence(A, B)

    A = "ABCD"
    B = "EACB"
    # 2
    print s.longestCommonSubsequence(A, B)


