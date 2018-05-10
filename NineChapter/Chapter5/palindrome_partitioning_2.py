# coding=utf-8
class Solution1(object):
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



# 2018-05-11 00:38
# 2018-05-11 01:53 Time Exceeded for calc m
# 2018-05-11 02:19 Time Exceeded for calc m

class Solution(object):
    def isPalindrom(self, s):
        for i in range(0, len(s) / 2):
            if s[i] != s[-i - 1]:
                return False
        return True

    def getPalindromMatrix1(self, s):
        # s[i: j] is palindrome = m[i][j]
        m = [x[:] for x in [[0] * (len(s) + 1)] * (len(s) + 1)]
        for i in range(0, len(s) + 1):
            for j in range(i, len(s) + 1):
                if self.isPalindrom(s[i: j]):
                    m[i][j] = 1

        return m

    def getPalindromMatrix(self, s):
        m = [x[:] for x in [[0] * (len(s) + 1)] * (len(s) + 1)]
        for i in range(0, len(s) + 1):
            m[i][i] = 1

        for i in range(0, len(s)):
            m[i][i + 1] = 1

        for i in range(0, len(s) - 1):
            if s[i] == s[i + 1]:
                m[i][i + 2] = 1

        for l in range(3, len(s) + 1):
            for i in range(0, len(s) - l + 1):
                if m[i + 1][i + l - 1] == 1:
                    if s[i] == s[i + l - 1]:
                        m[i][i + l] = 1

        return m

    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        m = self.getPalindromMatrix(s)

        a = [-1] # mincut in first i letter
        for i in range(0, len(s)):
            a.append(i)

        for i in range(0, len(s) + 1):
            for j in range(0, i + 1):
                if m[j][i] == 1:
                    if a[j] + 1 < a[i]:
                        a[i] = a[j] + 1
        return a[-1]


if __name__ == "__main__":
    s = Solution()

    # 1
    a = "abcccb"
    print s.minCut(a)

    # 1
    a = "aab"
    print s.minCut(a)

    # 0
    a = "bb"
    print s.minCut(a)

    #2
    a = "leet"
    print s.minCut(a)



