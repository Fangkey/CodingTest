# coding=utf-8


# 2018-05-26 16:07
# 2018-05-26 16:23

from random import randint

class RandomizedSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.vals = []
        self.pos = {}
        

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.pos:
            return False
        
        self.pos[val] = len(self.vals)
        self.vals.append(val)
        return True
        

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.pos:
            return False
        
        val_pos = self.pos[val]
        self.pos[self.vals[-1]] = val_pos
        self.vals[val_pos], self.vals[-1] = self.vals[-1], self.vals[val_pos]
        self.vals.pop()
        del self.pos[val]
        return True

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        i = randint(0, len(self.vals) - 1)
        return self.vals[i]
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()

if __name__ == "__main__":
    rs = RandomizedSet();
    
    # True
    print rs.insert(0)
    # True
    print rs.remove(0)
    # False
    print rs.remove(1)
    # True
    print rs.insert(2)
    # False
    print rs.insert(2)
    # True
    print rs.insert(3)
    # True
    print rs.insert(4)
    
    print rs.getRandom()
    print rs.getRandom()
    print rs.getRandom()
    print rs.getRandom()
