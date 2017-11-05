class Solution(object):
    def cvt10to3(self, num):
        num3 = 0
        cnt = 0
        while num != 0:
            num3 += (num % 3) * (10 ** cnt)
            num = num / 3
            cnt += 1

        return num3

    def cvt3to10(self, num):
        num10 = 0
        cnt = 0
        while num != 0:
            num10 = num10 + (3 ** cnt) * (num % 10)
            num = num /10
            cnt += 1
        return num10

    def xor3(self, num1, num2):
        sum = num1 + num2
        result = 0
        cnt = 0
        while sum != 0:
            result += (10 ** cnt) * (sum % 10 % 3)
            sum = sum / 10
            cnt += 1

        return result

    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum = 0
        cnt = 0
        for n in nums:
            if n < 0:
                n = -n
                cnt += 1
            sum = self.xor3(sum, self.cvt10to3(n))

        ret = self.cvt3to10(sum)
        if cnt % 3 != 0:
            ret = - ret
        return ret

class Solution2(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = 0
        bits = [0] * 32
        for i in range(0, 32):
            for n in nums:
                bits[i] += (n >> i) & 1
                bits[i] %= 3

            result |= (bits[i] << i)
        return result

if __name__ == "__main__":
    s = Solution()

    nums = [1, 1, 1, 2, 2, 2, 3, 4, 4, 4]
    print s.singleNumber(nums)

    nums = [-2, -2, 1, 1, -3, 1, -3, -3, -4, -2]
    print s.singleNumber(nums)