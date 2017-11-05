class Solution(object):
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        sum_ab = dict()
        for i in range(0, len(A)):
            a = A[i]
            for j in range(0, len(B)):
                b = B[j]
                s_ab = a + b
                if s_ab in sum_ab:
                    sum_ab[s_ab] += 1
                else:
                    sum_ab[s_ab] = 1

        sum_cd = dict()
        for i in range(0, len(C)):
            c = C[i]
            for j in range(0, len(D)):
                d = D[j]
                s_cd = c + d
                if s_cd in sum_cd:
                    sum_cd[s_cd] += 1
                else:
                    sum_cd[s_cd] = 1

        cnt = 0
        for key in sum_ab.keys():
            if -key in sum_cd:
                cnt += sum_ab[key] * sum_cd[-key]

        return cnt

if __name__ == "__main__":
    s = Solution()

    A = [1, 2]
    B = [-2, -1]
    C = [-1, 2]
    D = [0, 2]
    print s.fourSumCount(A, B, C, D)


