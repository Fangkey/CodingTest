#coding=utf-8
#2018-04-30 17:08
#2018-04-30 17:43

class Solution(object):
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return "Zero"

        segs = []
        str_num = str(num)
        i = len(str_num)
        while i > 0:
            s = i - 3
            if s < 0:
                s = 0

            e = i
            seg = str_num[s:e]
            segs.append(seg)

            i -= 3

        en_n = ""
        for i, seg in enumerate(segs):
            unit = ""
            if i == 0:
                unit = ""
            elif i == 1:
                unit = "Thousand"
            elif i == 2:
                unit = "Million"
            elif i == 3:
                unit = "Billion"

            en_seg = self.trans_3_digit(seg)
            if en_seg != "":
                en_n = en_seg + " " + unit + " " + en_n

        return en_n.strip()

    def trans_3_digit(self, str_3_digit):
        dict_digit = {
            1: "One",
            2: "Two",
            3: "Three",
            4: "Four",
            5: "Five",
            6: "Six",
            7: "Seven",
            8: "Eight",
            9: "Nine",

            10: "Ten",
            11: "Eleven",
            12: "Twelve",
            13: "Thirteen",
            14: "Fourteen",
            15: "Fifteen",
            16: "Sixteen",
            17: "Seventeen",
            18: "Eighteen",
            19: "Nineteen",

            20: "Twenty",
            30: "Thirty",
            40: "Forty",
            50: "Fifty",
            60: "Sixty",
            70: "Seventy",
            80: "Eighty",
            90: "Ninety"
        }

        n = int(str_3_digit)

        h = n / 100
        en_h = ""
        if h != 0:
            en_h = dict_digit[h]
            en_h = en_h + " Hundred"

        ten = n % 100
        en_ten = ""
        if ten <= 20 and ten > 0:
            en_ten = dict_digit[ten]
        else:
            ten_d = ten % 10
            ten_t = ten - ten_d

            en_ten_t = ""
            if ten_t != 0:
                en_ten_t = dict_digit[ten_t]

            en_ten_d = ""
            if ten_d != 0:
                en_ten_d = dict_digit[ten_d]
            if en_ten_d != 0:
                en_ten = en_ten_t + " " + en_ten_d

        en_h = " ".join([en_h, en_ten]).strip()

        return en_h


if __name__ == "__main__":
    s = Solution()

    print s.numberToWords(1000000)

    n = 2 ** 31 - 1
    # 2,147,483,647
    print n
    print s.numberToWords(n)