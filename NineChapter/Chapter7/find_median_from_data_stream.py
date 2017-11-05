from heapq import heappush, heappop

class MedianFinder(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.left_heap = []
        self.right_heap = []
        self.median = None

    def addNum(self, num):
        """
        :type num: int
        :rtype: void
        """
        if self.median is None:
            self.median = num
            return

        if num <= self.median:
            heappush(self.left_heap, num * -1)
            if len(self.left_heap) - len(self.right_heap) > 1:
                left_max = heappop(self.left_heap) * -1
                heappush(self.right_heap, self.median)
                self.median = left_max
        else:
            heappush(self.right_heap, num)
            if len(self.right_heap) - len(self.left_heap) > 1:
                right_min = heappop(self.right_heap)
                heappush(self.left_heap, -self.median)
                self.median = right_min

    def findMedian(self):
        """
        :rtype: float
        """
        if len(self.left_heap) == len(self.right_heap):
            return self.median
        elif len(self.left_heap) > len(self.right_heap):
            return (self.median - self.left_heap[0]) / 2.0
        else:
            return (self.median + self.right_heap[0]) / 2.0


if __name__ == "__main__":
    m = MedianFinder()
    print m.findMedian()
    m.addNum(12)
    print m.findMedian()
    m.addNum(10)
    print m.findMedian()
    m.addNum(13)
    print m.findMedian()
    m.addNum(11)
    print m.findMedian()
    m.addNum(5)
    print m.findMedian()
    m.addNum(15)
    print m.findMedian()
    m.addNum(1)
    print m.findMedian()
    m.addNum(11)
    print m.findMedian()
    m.addNum(6)
    print m.findMedian()
    m.addNum(17)
    print m.findMedian()
    m.addNum(14)
    print m.findMedian()
    m.addNum(8)
    print m.findMedian()