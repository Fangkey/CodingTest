class Solution1(object):
    def findTrans(self, wordList):
        trans_set = set()
        for i in range(0, len(wordList)):
            w1 = wordList[i]
            for j in range(i + 1, len(wordList)):
                w2 = wordList[j]
                if len(w1) == len(w2):
                    diff = 0
                    for k in range(0, len(w1)):
                        if w1[k] != w2[k]:
                            diff += 1
                        if diff > 1:
                            break
                    if diff == 1:
                        trans_set.add(w1 + " " + w2)
                        trans_set.add(w2 + " " + w1)

        return trans_set

    def helper(self, word_list, end_word, trans_set, cur_ladder, last_word, min_step):
        if last_word == end_word:
            if len(cur_ladder) < min_step[0] or min_step[0] == 0:
                min_step[0] = len(cur_ladder)
                return

        for i in range(0, len(word_list)):
            cur_word = word_list[i]
            if cur_word not in cur_ladder and last_word + " " + cur_word in trans_set:
                cur_ladder.add(cur_word)
                self.helper(word_list, end_word, trans_set, cur_ladder, cur_word, min_step)
                cur_ladder.discard(cur_word)

    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        wordList.append(beginWord)
        trans_set = self.findTrans(wordList)
        wordList.pop()
        min_step = [0]
        cur_ladder = set()
        cur_ladder.add(beginWord)
        self.helper(wordList, endWord, trans_set, cur_ladder, beginWord, min_step)
        return min_step[0]



class Solution(object):
    def getNeighbors(self, word, word_set):
        neighbors = []

        for i in range(0, len(word)):
            for l in range(ord('a'), ord('z') + 1):
                new_word = word[0:i] + chr(l) + word[i + 1:]
                if new_word in word_set:
                    neighbors.append(new_word)
        return neighbors


    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        if len(wordList) == 0:
            return 0

        word_set = set()
        for w in wordList:
            word_set.add(w)

        if endWord not in word_set:
            return 0

        word_set.add(beginWord)
        word_set.add(endWord)

        if len(word_set) == 1:
            return 0

        node_queue = []
        node_queue.append(beginWord)
        start = 0

        ladder_dict = dict()
        ladder_dict[beginWord] = 1
        while start < len(node_queue):
            cur_node = node_queue[start]
            start += 1
            cur_size = ladder_dict[cur_node]
            for n in self.getNeighbors(cur_node, word_set):
                if n == endWord:
                    return cur_size + 1
                else:
                    if not n in ladder_dict:
                        node_queue.append(n)
                        ladder_dict[n] = cur_size + 1
        return 0

if __name__ == "__main__":
    s = Solution()

    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot", "dot", "dog", "lot", "log"]
    # 0
    print s.ladderLength(beginWord, endWord, wordList)

    beginWord = "talk"
    endWord = "tail"
    wordList = ["talk", "tons", "fall", "tail", "gale", "hall", "negs"]
    # 0
    print s.ladderLength(beginWord, endWord, wordList)

    beginWord = "hot"
    endWord = "dog"
    wordList = ["hot", "dog"]
    # 0
    print s.ladderLength(beginWord, endWord, wordList)

    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
    # 5
    print s.ladderLength(beginWord, endWord, wordList)

    beginWord = "hot"
    endWord = "dog"
    wordList = ["hot", "dog", "dot"]
    # 3
    print s.ladderLength(beginWord, endWord, wordList)

    beginWord = "hit"
    endWord = "zzz"
    wordList = ["hot", "dot", "dog", "lot", "log", "cog", "zzz"]
    # 0
    print s.ladderLength(beginWord, endWord, wordList)

    beginWord = "hit"
    endWord = "hit"
    wordList = ["hit"]
    # 0
    print s.ladderLength(beginWord, endWord, wordList)

    beginWord = "hit"
    endWord = "his"
    wordList = []
    # 0
    print s.ladderLength(beginWord, endWord, wordList)