#coding=utf-8

# 2018-04-29 0:21
# 2018-04-29 0:38

class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """

        t = num / 1000
        h = (num % 1000) / 100
        e = (num % 100) / 10
        d = (num % 10)

        tr = ""
        if t == 1:
            tr = "M"
        elif t == 2:
            tr = "MM"
        elif t == 3:
            tr = "MMM"

        hr = ""
        if h == 1:
            hr = "C"
        elif h == 2:
            hr = "CC"
        elif h == 3:
            hr = "CCC"
        elif h == 4:
            hr = "CD"
        elif h == 5:
            hr = "D"
        elif h == 6:
            hr = "DC"
        elif h == 7:
            hr = "DCC"
        elif h == 8:
            hr = "DCCC"
        elif h == 9:
            hr = "CM"

        er = ""
        if e == 1:
            er = "X"
        elif e == 2:
            er = "XX"
        elif e == 3:
            er = "XXX"
        elif e == 4:
            er = "XL"
        elif e == 5:
            er = "L"
        elif e == 6:
            er = "LX"
        elif e == 7:
            er = "LXX"
        elif e == 8:
            er = "LXXX"
        elif e == 9:
            er = "XC"

        dr = ""
        if d == 1:
            dr = "I"
        elif d == 2:
            dr = "II"
        elif d == 3:
            dr = "III"
        elif d == 4:
            dr = "IV"
        elif d == 5:
            dr = "V"
        elif d == 6:
            dr = "VI"
        elif d == 7:
            dr = "VII"
        elif d == 8:
            dr = "VIII"
        elif d == 9:
            dr = "IX"

        return tr + hr + er + dr


if __name__ == "__main__":
    s = Solution()

    print s.intToRoman(3)

    print s.intToRoman(4)

    print s.intToRoman(9)

    print s.intToRoman(58)

    print s.intToRoman(1994)