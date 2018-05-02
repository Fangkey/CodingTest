# coding = utf-8
# 2018-05-01 22:17
# 2018-05-01 22:34 permutation, time exceeded

# 2018-05-01 23:57 Accepted. Zero, Segment

class Solution1(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == "":
            return 0

        if s[0] == '0':
            return 0

        for i, l in enumerate(list(s)):
            if l == "0" and i != 0:
                if not (s[i - 1] == "1" or s[i - 1] == "2"):
                    return 0

        amb_segs = []
        i = 0
        si = 0
        start = False
        while i < len(s) - 1:
            start = False
            for j in range(i, len(s)):
                seg = int(s[j: j + 2])
                if not start:
                    if seg >= 11 and seg <= 26:
                        start = True
                        si = j
                    else:
                        i += 1
                else:
                    if not (seg >= 10 and seg <= 26):
                        amb_segs.append(s[si: j + 1])
                        i = j + 1
                        start = False
                        break

        if start:
            amb_segs.append(s[si: ])

        count = 1
        for seg in amb_segs:
            count *= self.get_count(seg)

        return count

    def get_count(self, s):
        if int(s) < 1:
            return 0

        count = [0]
        self.helper(s, 0, count)
        return count[0]

    def helper(self, s, n, count):
        if n == len(s):
            count[0] += 1
            return

        d1 = s[n]
        if d1 == '0':
            return

        self.helper(s, n + 1, count)
        if n + 1 < len(s):
            d2 = s[n: n + 2]
            if int(d2) <= 26:
                self.helper(s, n + 2, count)


# DP Solution
# 2018-05-02 23:03
# 2018-05-02 23:33

class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == "" or s[0] == '0':
            return 0

        # a[i] is the decode ways of the first i char
        a = [0] * (len(s) + 1)
        a[0] = 1
        a[1] = 1

        for i in range(1, len(s)):
            c = s[i]
            bc = s[i - 1]
            if c == "0" and not (bc == "1" or bc == "2"):
                return 0

            if bc == "1" and c >= "1" and c <= "9":
                # need judge ss[i + 1] == "0"
                if i < len(s) - 1:
                    if s[i + 1] == "0":
                        a[i + 1] = a[i]
                    else:
                        a[i + 1] = a[i] + a[i - 1]
                else:
                    a[i + 1] = a[i] + a[i - 1]
            elif bc == "2" and c >= "1" and c <= "6":
                if i < len(s) - 1:
                    if s[i + 1] == "0":
                        a[i + 1] = a[i]
                    else:
                        a[i + 1] = a[i] + a[i - 1]
                else:
                    a[i + 1] = a[i] + a[i - 1]
            else:
                a[i + 1] = a[i]

        return a[-1]


if __name__ == "__main__":
    s = Solution()
    # 3
    print s.numDecodings("12120")
    # 0
    print s.numDecodings("100")
    # 0
    print s.numDecodings("230")
    # 1
    print s.numDecodings("101")
    # 1
    print s.numDecodings("110")
    # 2
    print s.numDecodings("227")
    # 0
    print s.numDecodings("01")
    # 0
    print s.numDecodings("100")
    # 1
    print s.numDecodings("1")
    # 589824
    print s.numDecodings("4757562545844617494555774581341211511296816786586787755257741178599337186486723247528324612117156948")
    # 1
    print s.numDecodings("10")
    # 2
    print s.numDecodings("12")
    # 3
    print s.numDecodings("226")

