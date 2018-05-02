# coding=utf-8
# 2018-04-30 20:02
# 2018-04-30 20:10

class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        la = len(a)
        lb = len(b)
        l = max(la, lb)

        if la > lb:
            b = "0" * (la - lb) + b
        else:
            a = "0" * (lb - la) + a

        inc = 0
        res = ""
        for i in range(l - 1, -1, -1):
            r = int(a[i]) + int(b[i]) + inc
            inc = r / 2
            res = str(r%2) + res

        if inc == 1:
            res = "1" + res

        return res

if __name__ == "__main__":
    s = Solution()

    a = "11"
    b = "1"
    # 100
    print s.addBinary(a, b)

    a = "1010"
    b = "1011"
    # 10101
    print s.addBinary(a, b)

    a = "0"
    b = "01"
    print s.addBinary(a, b)

