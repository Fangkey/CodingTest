class Solution(object):
    def buildTrie(self, words):
        trie = dict()
        for w in words:
            cur_dict = trie
            w = w + " "
            for l in w:
                if l in cur_dict:
                    cur_dict = cur_dict[l]
                else:
                    cur_dict[l] = dict()
                    cur_dict = cur_dict[l]
        return trie

    def findInTrie(self, trie, word):
        cur_dict = trie
        for l in word:
            if l in cur_dict:
                cur_dict = cur_dict[l]
            else:
                return False, None
        return True, cur_dict

    def helper(self, board, m, n, i, j, cur_trie, cur_word, trace, result):
        if i >= m or i < 0 or j >= n or j < 0:
            return

        if (i, j) in trace:
            return

        l = board[i][j]
        found, new_trie = self.findInTrie(cur_trie, l)
        if found:
            new_word = cur_word + l
            if " " in new_trie:
                result.add(new_word)

            trace.append((i, j))
            # right
            new_trace = trace[:]
            self.helper(board, m, n, i, j + 1, new_trie, new_word, new_trace, result)
            # down
            new_trace = trace[:]
            self.helper(board, m, n, i + 1, j, new_trie, new_word, new_trace, result)
            # up
            new_trace = trace[:]
            self.helper(board, m, n, i - 1, j, new_trie, new_word, new_trace, result)
            # left
            new_trace = trace[:]
            self.helper(board, m, n, i, j - 1, new_trie, new_word, new_trace, result)
            trace.pop()
        else:
            return

    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        m = len(board)
        if m == 0:
            return []

        n = len(board[0])
        if n == 0:
            return []

        trie = self.buildTrie(words)

        result = set()
        for i in range(0, m):
            for j in range(0, n):
                trace = []
                self.helper(board, m, n, i, j, trie, "", trace, result)

        return list(result)


if __name__ == "__main__":
    s = Solution()

    board = [["a","b"],["a","a"]]
    words = ["aba","baa","bab","aaab","aaa","aaaa","aaba"]
    #words = ["aaab"]
    # ["aaa","aaab","aaba","aba","baa"]
    # continue to find when letter found
    print s.findWords(board, words)


    board = [["a", "b"], ["c", "d"]]
    words = ["acdb"]
    # ["acdb"]
    print s.findWords(board, words)

    board = [["a", "a"]]
    words = ["aaa"]
    # []
    # no back
    print s.findWords(board, words)


    board = [["a","a"]]
    words = ["a"]
    # ['a']
    # distinct
    print s.findWords(board, words)

    board = [
      ['o','a','a','n'],
      ['e','t','a','e'],
      ['i','h','k','r'],
      ['i','f','l','v']
    ]
    words = ["oath", "pea", "eat", "rain"]
    # ['oath', 'eat']
    print s.findWords(board, words)