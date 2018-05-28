# coding=utf-8

# 2018-05-10 01:43
# 2018-05-10 02:03

class Solution1(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        for i in range(0, len(citations)):
            c = citations[i]
            if c >= len(citations) - i:
                return len(citations) - i
        return 0

# 2018-05-10 02:03
# 2018-05-10 02:58
class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        if len(citations) == 0:
            return 0

        start = 0
        end = len(citations) - 1
        while start + 1 < end:
            mid = start + (end - start) /2
            c = citations[mid]

            if c < len(citations) - mid:
                start = mid
            else:
                end = mid

        if citations[start] >= len(citations) - start:
            return len(citations) - start
        elif citations[end] >= len(citations) - end:
            return len(citations) - end
        else:
            return 0

if __name__ == "__main__":
    s = Solution()

    # 3
    citations = [1, 1, 1, 1, 1, 100, 100, 100]
    print s.hIndex(citations)

    # 1
    citations = [1]
    print s.hIndex(citations)

    # 0
    citations = []
    print s.hIndex(citations)

    # 1
    citations = [1, 1]
    print s.hIndex(citations)

    # 0
    citations = [0]
    print s.hIndex(citations)

    # 3
    citations = [3, 0, 6, 1, 5]
    print s.hIndex(citations)

    # 2
    citations = [0, 1, 2, 3, 6]
    print s.hIndex(citations)


