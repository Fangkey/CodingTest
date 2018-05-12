# coding=utf-8
class Solution1(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        word_set = set()
        for w in wordDict:
            word_set.add(w)

        f = [False] * (len(s) + 1)
        f[0] = True
        for i in range(0, len(s)):
            for j in range(0, i + 1):
                if f[j] is True and s[j: i + 1] in word_set:
                    f[i + 1] = True

        return f[-1]


# 2018-05-13 02:10
# 2018-05-13 02:24

class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        word_set = set()
        for w in wordDict:
            word_set.add(w)

        a = [False] * (len(s) + 1)
        a[0] = True

        for i in range(0, len(s)):
            for j in range(0, i + 1):
                if a[j] and s[j: i + 1] in word_set:
                    a[i + 1] = True
                    break
        return a[-1]


if __name__ == "__main__":
    s = Solution()

    a = "a"
    dict = ["a"]
    print s.wordBreak(a, dict)

    # True
    a = "leetcode"
    dict = ["leet", "code"]
    print s.wordBreak(a, dict)

    # False
    a = "letcode"
    dict = ["leet", "code"]
    print s.wordBreak(a, dict)


