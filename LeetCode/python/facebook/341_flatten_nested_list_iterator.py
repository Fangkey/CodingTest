# coding=utf-8
# 2018-05-04 00:20
# 2018-05-04 00:59 has_next is hard, use to_next()

# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
# class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class NestedIterator(object):
    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.nested_list = nestedList
        self.cur_list = []
        self.cur_i = 0
        self.stack = []
        self.next_int = None

        if len(self.nested_list) != 0:
            self.cur_list = self.nested_list
            self.stack.append((self.cur_list, 0))

        self.next_int = self.to_next()

    def to_next(self):
        if len(self.stack) == 0:
            return None

        if self.cur_i < len(self.cur_list) and self.cur_list[self.cur_i].isInteger():
            ret_int = self.cur_list[self.cur_i].getInteger()
            self.cur_i += 1
            return ret_int
        elif self.cur_i == len(self.cur_list):
            while self.cur_i == len(self.cur_list) and len(self.stack) != 0:
                self.cur_list, self.cur_i = self.stack.pop()
                self.cur_i += 1
            return self.to_next()
        else:
            while self.cur_i < len(self.cur_list) and not self.cur_list[self.cur_i].isInteger():
                if len(self.cur_list[self.cur_i].getList()) == 0:
                    self.cur_i += 1
                else:
                    self.stack.append((self.cur_list, self.cur_i))
                    self.cur_list = self.cur_list[self.cur_i].getList()
                    self.cur_i = 0
            return self.to_next()


    def next(self):
        """
        :rtype: int
        """
        ret_int = self.next_int
        self.next_int = self.to_next()
        return ret_int


    def hasNext(self):
        """
        :rtype: bool
        """
        if self.next_int is None:
            return False
        else:
            return True





        # Your NestedIterator object will be instantiated and called as such:
        # i, v = NestedIterator(nestedList), []
        # while i.hasNext(): v.append(i.next())