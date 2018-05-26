# coding=utf-8

# 2018-05-26 12:06
# 2018-05-26 12:17

class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = dict()
        

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        cur_root = self.root
        for l in word:
            if l in cur_root:
                cur_root = cur_root[l]
            else:
                cur_root[l] = dict()
                cur_root = cur_root[l]
        cur_root[0] = True
        

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        cur_root = self.root
        for l in word:
            if l in cur_root:
                cur_root = cur_root[l]
            else:
                return False
            
        if 0 in cur_root:
            return True
        else:
            return False
        

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        cur_root = self.root
        for l in prefix:
            if l in cur_root:
                cur_root = cur_root[l]
            else:
                return False
            
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

if __name__ == "__main__":
    trie = Trie()
    
    trie.insert("main")
    trie.insert("man")
    trie.insert("many")
    trie.insert("aaa")
    
    # True
    print trie.search("aaa")
    # True
    print trie.search("main")
    # False
    print trie.search("ma")
    # True
    print trie.startsWith("ma")