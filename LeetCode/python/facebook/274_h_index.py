# coding=utf-8

# 2018-05-11 00:11
# 2018-05-11 00:56

class Solution1(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        sc = sorted(citations)
        for i in range(len(sc) - 1, -1, -1):
            c_up = sc[i]
            if i == 0:
                c_low = -1
            else:
                c_low = sc[i - 1]

            if len(sc) - i <= c_up and len(sc) - i >= c_low:
                return len(sc) - i
        return 0

# 2018-05-10 01:09
# 2018-05-10 01:39

class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        len_c = len(citations)
        bucket = [0] * len_c
        for c in citations:
            if c >= len_c:
                bucket[len_c - 1] += 1
            elif c > 0:
                bucket[c - 1] += 1

        sum = 0
        for i in range(len(bucket) - 1, -1, -1):
            s = bucket[i]
            sum += s
            if sum >= i + 1:
                return i + 1
        return 0


if __name__ == "__main__":
    s = Solution()

    # 1
    citations = [1, 1, 100, 100, 100]
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