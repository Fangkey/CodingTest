class MyQueue(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.push_stack = []
        self.pop_stack = []

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: void
        """
        self.push_stack.append(x)

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        if len(self.pop_stack) == 0:
            while len(self.push_stack) != 0:
                self.pop_stack.append(self.push_stack.pop())

        return self.pop_stack.pop()

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        if len(self.pop_stack) == 0:
            while len(self.push_stack) != 0:
                self.pop_stack.append(self.push_stack.pop())

        ret = self.pop_stack.pop()
        self.pop_stack.append(ret)

        return ret

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        if len(self.push_stack) == 0 and len(self.pop_stack) == 0:
            return True
        else:
            return False


if __name__ == "__main__":
    s = MyQueue()
    print s.empty()

    s.push(7)
    s.push(9)
    s.push(10)
    s.push(2)
    s.push(1)

    print s.empty()

    print s.peek()
    print s.pop()

    print s.peek()
    print s.pop()

    print s.peek()
    print s.pop()

    print s.peek()
    print s.pop()

    print s.peek()
    print s.pop()