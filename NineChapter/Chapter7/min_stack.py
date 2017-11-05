class MinStack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min_stack = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.stack.append(x)
        if len(self.min_stack) == 0:
            self.min_stack.append(x)
        else:
            cur_min = self.min_stack[-1]
            if x < cur_min:
                self.min_stack.append(x)
            else:
                self.min_stack.append(cur_min)

    def pop(self):
        """
        :rtype: void
        """
        if len(self.stack) != 0:
            self.stack.pop()
            self.min_stack.pop()

    def top(self):
        """
        :rtype: int
        """
        if len(self.stack) != 0:
            return self.stack[-1]
        else:
            return None

    def getMin(self):
        """
        :rtype: int
        """
        if len(self.min_stack) != 0:
            return self.min_stack[-1]
        else:
            return None


if __name__ == "__main__":
    s = MinStack()

    s.push(7)
    s.push(9)
    s.push(10)
    s.push(2)
    s.push(1)

    print s.getMin()
    s.pop()

    print s.getMin()
    s.pop()

    print s.getMin()
    s.pop()

    print s.getMin()
    s.pop()

    print s.getMin()
    s.pop()

    print s.getMin()
    s.pop()
