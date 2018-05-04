# coding = utf-8
# 2018-05-05 01:12
# 2018-05-05 01:23 Corner case: 1993

class Solution(object):
    def maximumSwap(self, num):
        """
        :type num: int
        :rtype: int
        """
        n = str(num)
        n = [int(d) for d in n]
        max_diff = 0
        max_i = -1
        max_j = -1
        for i in range(0, len(n)):
            s = n[i]
            for j in range(i, len(n)):
                e = n[j]
                if s < e:
                    # important
                    if e - s >= max_diff:
                        max_diff = e - s
                        max_i = i
                        max_j = j
            if max_diff != 0:
                break

        if max_diff != 0:
            n[max_i], n[max_j] = n[max_j], n[max_i]

        return int("".join([str(d) for d in n]))

if __name__ == "__main__":
    s = Solution()

    n = 2736
    print s.maximumSwap(n)

    n = 1993
    print s.maximumSwap(n)