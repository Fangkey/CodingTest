class Solution(object):
    def helper(self, s, word_set, cur_index, cur_segs, result):
        if cur_index > len(s) - 1:
            result.append(cur_segs[:])
            return

        for i in range(cur_index, len(s)):
            if s[cur_index: i + 1] in word_set:
                cur_segs.append(s[cur_index: i + 1])
                self.helper(s, word_set, i + 1, cur_segs, result)
                cur_segs.pop()

    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        if len(s) == 0:
            return []

        word_set = set()
        for w in wordDict:
            word_set.add(w)

        cur_index = 0
        cur_segs = []
        result = []
        self.helper(s, word_set, cur_index, cur_segs, result)

        ret = []
        for segs in result:
            ret.append(" ".join(segs))

        return ret

if __name__ == "__main__":
    s = Solution()

    a = ""
    dict = ["cat", "cats", "and", "sand", "dog"]
    print s.wordBreak(a, dict)

    a = "catsanddog"
    dict = ["cat", "cats", "and", "sand", "dog"]
    print s.wordBreak(a, dict)

    a = "casanddog"
    dict = ["cat", "cats", "and", "sand", "dog"]
    print s.wordBreak(a, dict)

