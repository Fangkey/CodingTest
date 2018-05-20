# coding=utf-8

# 2018-05-20 02:41
# 2018-05-20 03:34 TLE
# 2018-05-20 03:46

class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if s == "" and p == "":
            return True
        elif s != "" and p == "":
            return False

        a = [x[:] for x in [[False] * (len(p) + 1)] * (len(s) + 1)]
        a[0][0] = True

        for j in range(0, len(p)):
            if p[j] == "*":
                for i in range(0, len(s) + 1):
                    a[i][j + 1] = True
            else:
                break

        for i in range(0, min(len(s), len(p))):
            if s[i].isalpha() and p[i].isalpha():
                if s[i] != p[i]:
                    return False
            else:
                break

        for j in range(0, len(p)):
            for i in range(0, len(s)):
                if a[i + 1][j + 1]:
                    # pre-calc-ed
                    continue
                if p[j] == "*":
                    for k in range(0, i + 2):
                        if a[k][j]:
                            # important, pre-calc all after-condition
                            for m in range(i + 1, len(s) + 1):
                                a[m][j + 1] = True
                            break
                elif p[j] == "?":
                    if a[i][j] == True:
                        a[i + 1][j + 1] = True
                else:
                    if s[i] == p[j] and a[i][j]:
                        a[i + 1][j + 1] = True

        return a[-1][-1]

if __name__ == "__main__":
    sl = Solution()

    s = "ho"
    p = "**ho"
    # True
    print sl.isMatch(s, p)

    s = "mississippi"
    p = "m??*ss*?i*pi"
    # False
    print sl.isMatch(s, p)

    s = "a"
    p = "a*"
    # True
    print sl.isMatch(s, p)

    s = ""
    p = "*"
    # True
    print sl.isMatch(s, p)

    s = ""
    p = ""
    # True
    print sl.isMatch(s, p)

    s = "adceb"
    p = "*a*b"
    # True
    print sl.isMatch(s, p)

    s = "aa"
    p = "*"
    # True
    print sl.isMatch(s, p)

    s = "aa"
    p = "a"
    # False
    print sl.isMatch(s, p)

    s = "cb"
    p = "?a"
    # False
    print sl.isMatch(s, p)

    s = "acdcb"
    p = "a*c?b"
    # False
    print sl.isMatch(s, p)