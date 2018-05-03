# coding=utf-8


# 2018-05-03 23:29
# 2018-05-03 23:58 Sort first, Merge in place

# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        intervals = sorted(intervals, key=lambda d: d.start)

        new_intervals = []

        for i in intervals:
            if len(new_intervals) == 0:
                new_intervals.append(i)
            elif new_intervals[-1].end >= i.start:
                if new_intervals[-1].end < i.end:
                    new_intervals[-1].end = i.end
            else:
                new_intervals.append(i)

        return new_intervals


def print_intervals(intervals):
    ss = []
    for i in intervals:
        ss.append("[" + str(i.start) + "," + str(i.end) + "]")

    print " ".join(ss)


if __name__ == "__main__":
    s = Solution()

    # [1,6] [8,10] [15,18]
    interval = [Interval(1, 3), Interval(2, 6), Interval(8, 10), Interval(15, 18)]
    print_intervals(s.merge(interval))

    # [1,5]
    interval = [Interval(1,4),Interval(4,5)]
    print_intervals(s.merge(interval))