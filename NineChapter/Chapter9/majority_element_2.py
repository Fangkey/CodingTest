class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if len(nums) == 0:
            return []

        cand1 = None
        cand2 = None
        cnt1 = 0
        cnt2 = 0

        for n in nums:
            if n == cand1:
                cnt1 += 1
            elif n == cand2:
                cnt2 += 1
            elif cnt1 == 0:
                cand1 = n
                cnt1 = 1
            elif cnt2 == 0:
                cand2 = n
                cnt2 = 1
            else:
                cnt1 -= 1
                cnt2 -= 1

        cnt1 = 0
        cnt2 = 0
        for n in nums:
            if n == cand1:
                cnt1 += 1
            elif n == cand2:
                cnt2 += 1

        ret = []
        if cnt1 > len(nums) / 3.0:
            ret.append(cand1)
        if cnt2 > len(nums) / 3.0:
            ret.append(cand2)

        return ret


if __name__ == "__main__":
    s = Solution()

    nums = [1]
    print s.majorityElement(nums)

    nums = [1, 1, 1, 2, 2, 2, 3, 3]
    print s.majorityElement(nums)