class Solution(object):
    def getIsPalindrome(self, s):
        m = [x[:] for x in [[False] * len(s)] * len(s)]

        for i in range(0, len(s)):
            m[i][i] = True

        for i in range(0, len(s) - 1):
            if s[i] == s[i + 1]:
                m[i][i + 1] = True

        for length in range(3, len(s) + 1):
            for i in range(0, len(s) - length + 1):
                if s[i] == s[i +length - 1] and m[i + 1][i + length - 2] is True:
                    m[i][i +length - 1] = True
        return m


    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        isParlindrome = self.getIsPalindrome(s)
        f = [i for i in range(-1, len(s))]

        for i in range(0, len(s)):
            for j in range(0, i + 1):
                if isParlindrome[j][i]:
                    if f[i + 1] > f[j] + 1:
                        f[i + 1] = f[j] + 1
        return f[-1]


if __name__ == "__main__":
    s = Solution()

    a = "abcccb"
    print s.minCut(a)

    a = "leet"
    print s.minCut(a)

    a = "aab"
    print s.minCut(a)

