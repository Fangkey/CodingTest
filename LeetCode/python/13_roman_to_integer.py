#coding=utf-8

# 2018-04-29 0:48
# 2018-04-29 1:03

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        t = 0

        if s.find("MMM") == 0:
            t = 3
            s = s[3:]
        elif s.find("MM") == 0:
            t = 2
            s = s[2:]
        elif s.find("M") == 0:
            t = 1
            s = s[1:]

        h = 0
        if s.find("CM") == 0:
            h = 9
            s = s[2:]
        elif s.find("DCCC") == 0:
            h = 8
            s = s[4:]
        elif s.find("DCC") == 0:
            h = 7
            s = s[3:]
        elif s.find("DC") == 0:
            h = 6
            s = s[2:]
        elif s.find("D") == 0:
            h = 5
            s = s[1:]
        elif s.find("CD") == 0:
            h = 4
            s = s[2:]
        elif s.find("CCC") == 0:
            h = 3
            s = s[3:]
        elif s.find("CC") == 0:
            h = 2
            s = s[2:]
        elif s.find("C") == 0:
            h = 1
            s = s[1:]

        e = 0
        if s.find("XC") == 0:
            e = 9
            s = s[2:]
        elif s.find("LXXX") == 0:
            e = 8
            s = s[4:]
        elif s.find("LXX") == 0:
            e = 7
            s = s[3:]
        elif s.find("LX") == 0:
            e = 6
            s = s[2:]
        elif s.find("L") == 0:
            e = 5
            s = s[1:]
        elif s.find("XL") == 0:
            e = 4
            s = s[2:]
        elif s.find("XXX") == 0:
            e = 3
            s = s[3:]
        elif s.find("XX") == 0:
            e = 2
            s = s[2:]
        elif s.find("X") == 0:
            e = 1
            s = s[1:]

        d = 0
        if s.find("IX") == 0:
            d = 9
        elif s.find("VIII") == 0:
            d = 8
        elif s.find("VII") == 0:
            d = 7
        elif s.find("VI") == 0:
            d = 6
        elif s.find("V") == 0:
            d = 5
        elif s.find("IV") == 0:
            d = 4
        elif s.find("III") == 0:
            d = 3
        elif s.find("II") == 0:
            d = 2
        elif s.find("I") == 0:
            d = 1

        return t * 1000 + h * 100 + e * 10 + d


if __name__ == "__main__":
    s = Solution()

    print s.romanToInt("III")

    print s.romanToInt("IV")

    print s.romanToInt("IX")

    print s.romanToInt("LVIII")

    print s.romanToInt("MCMXCIV")