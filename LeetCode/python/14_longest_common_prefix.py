# coding=utf-8

# 2018-04-29 1:06
# 2018-04-29 1:27

# notice a common finish differs from a unmatch finish

class Solution1(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        cp = ""
        i = 0
        while True:
            cc = ""
            stop = False
            for s in strs:
                if len(s) > i:
                    c = s[i]
                    if cc == "":
                        cc = c
                    elif c != cc:
                        stop = True
                        cc = ""
                        break
                else:
                    stop = True
                    cc = ""
                    break

            if stop:
                break

            cp += cc
            i += 1

        return cp

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ""

        if len(strs) == 1:
            return strs[0]

        s0 = strs[0]
        finish = False
        p = ""
        for i in range(0, len(s0)):
            p = s0[0: i + 1]
            for s in strs[1:]:
                if s.find(p) != 0:
                    finish = True
                    p = p[0: -1]
                    break
            if finish:
                break

        return p

if __name__ == "__main__":
    s = Solution()
    print s.longestCommonPrefix(["c", "c"])

    print s.longestCommonPrefix(["a"])

    print s.longestCommonPrefix(["flower","flow","flight"])

    print s.longestCommonPrefix(["dog","racecar","car"])