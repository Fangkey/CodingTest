# coding=utf-8
#2018-05-05 01:05
#2018-05-05 01:10

class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        n1 = []
        for i in range(len(num1) - 1, -1, -1):
            n1.append(int(num1[i]))

        n2 = []
        for i in range(len(num2) - 1, -1, -1):
            n2.append(int(num2[i]))

        sum = 0
        for i in range(0, len(n1)):
            for j in range(0, len(n2)):
               sum += n1[i] * n2[j] * 10 ** (i + j)

        return str(sum)


if __name__ == "__main__":
    s = Solution()

    num1 = "123"
    num2 = "456"
    # 56088
    print s.multiply(num1, num2)