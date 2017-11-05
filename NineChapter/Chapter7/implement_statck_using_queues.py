from collections import deque

class MyStack(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue1 = deque([])
        self.queue2 = deque([])

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: void
        """
        self.queue1.append(x)

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        for i in range(0, len(self.queue1) - 1):
            self.queue2.append(self.queue1.popleft())

        ret = self.queue1.popleft()

        for i in range(0, len(self.queue2)):
            self.queue1.append(self.queue2.popleft())

        return ret

    def top(self):
        """
        Get the top element.
        :rtype: int
        """

        for i in range(0, len(self.queue1) - 1):
            self.queue2.append(self.queue1.popleft())

        ret = self.queue1.popleft()

        for i in range(0, len(self.queue2)):
            self.queue1.append(self.queue2.popleft())

        self.queue1.append(ret)

        return ret

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        if len(self.queue1) == 0:
            return True

        return False