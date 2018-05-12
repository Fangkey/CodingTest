class Solution1(object):
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

# 2018-05-13 02:26
# 2018-05-13 03:23 LTE
# 2018-05-13 03:40

class Solution(object):
    def find_sentence(self, s, max_len, word_set):
        if s in self.mems:
            return self.mems[s]

        s_set = set()
        if s in word_set:
            s_set.add(s)

        len_s = min(max_len + 1, len(s))
        for i in range(1, len_s):
            ls = self.find_sentence(s[0:i], max_len, word_set)
            if len(ls) != 0: # important
                rs = self.find_sentence(s[i:], max_len, word_set)
                if len(rs) != 0: # important
                    for l in ls:
                        for r in rs:
                            s_set.add(l + " " + r)
        self.mems[s] = s_set
        return s_set

    def pre_check(self, s, wordDict):
        letter_set = set()
        for w in wordDict:
            for l in w:
                letter_set.add(l)

        for l in s:
            if l not in letter_set:
                return False

        return True

    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        if len(wordDict) == 0:
            return []

        if not self.pre_check(s, wordDict):
            return []

        word_set = set()
        for w in wordDict:
            word_set.add(w)

        max_len = max([len(w) for w in wordDict])
        self.mems = {}
        all_sentence = self.find_sentence(s, max_len, word_set)
        return list(all_sentence)




if __name__ == "__main__":
    s = Solution()

    a = "catsanddog"
    dict = ["cat", "cats", "and", "sand", "dog"]
    print s.wordBreak(a, dict)

    a = "a"
    dict = []
    print s.wordBreak(a, dict)

    a = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    dict = ["aa", "aaa", "aaaa", "aaaaa", "aaaaaa", "aaaaaaa", "aaaaaaaa", "aaaaaaaaa", "aaaaaaaaaa", "ba"]
    print s.wordBreak(a, dict)

    a = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    dict = ["a", "aa", "aaa", "aaaa", "aaaaa", "aaaaaa", "aaaaaaa", "aaaaaaaa", "aaaaaaaaa", "aaaaaaaaaa"]
    print s.wordBreak(a, dict)

    a = ""
    dict = ["cat", "cats", "and", "sand", "dog"]
    print s.wordBreak(a, dict)

    a = "casanddog"
    dict = ["cat", "cats", "and", "sand", "dog"]
    print s.wordBreak(a, dict)

