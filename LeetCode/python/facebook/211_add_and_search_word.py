# coding = utf-8
# 2018-05-04 00:00
# 2018-05-04 00:29

class WordDictionary(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = {}

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        cur_root = self.root
        for l in word:
            if l in cur_root:
                cur_root = cur_root[l]
            else:
                cur_root[l] = {}
                cur_root = cur_root[l]

        # leaf should be a dict
        cur_root[0] = {}

    def helper(self, word, cur_index, cur_root):
        if cur_index == len(word):
            if 0 in cur_root:
                return True
            else:
                return False

        l = word[cur_index]
        if l != ".":
            if l in cur_root:
                cur_root = cur_root[l]
                return self.helper(word, cur_index + 1, cur_root)
            else:
                return False
        else:
            found = False
            for key in cur_root.keys():
                found = found or self.helper(word, cur_index + 1, cur_root[key])
            return found

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        return self.helper(word, 0, self.root)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)

if __name__ == "__main__":
    obj = WordDictionary()

    # obj.addWord("bad")
    # obj.addWord("dad")
    # obj.addWord("mad")
    # # False
    # print obj.search("pad")
    # # True
    # print obj.search("bad")
    # # True
    # print obj.search(".ad")
    # # True
    # print obj.search("b..")


    obj.addWord("a")
    obj.addWord("a")
    print obj.search("a.")
    # True
    print obj.search(".")
    # True
    print obj.search("a")
    # False
    print obj.search("aa")
    # True
    print obj.search("a")
    # False
    print obj.search(".a")
