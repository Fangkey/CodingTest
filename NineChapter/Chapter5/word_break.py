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

        f = [False] * (len(s) + 1)
        f[0] = True
        for i in range(0, len(s)):
            for j in range(0, i + 1):
                if f[j] is True and s[j: i + 1] in word_set:
                    f[i + 1] = True

        return f[-1]


if __name__ == "__main__":
    s = Solution()

    a = "leetcode"
    dict = ["leet", "code"]
    print s.wordBreak(a, dict)

    a = "letcode"
    dict = ["leet", "code"]
    print s.wordBreak(a, dict)


