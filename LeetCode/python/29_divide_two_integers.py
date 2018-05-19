# coding=utf-8

# 2018-05-17:12:09
# 2018-05-17:12:18 TLE

class Solution1(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        
        sign = 1
        if dividend < 0:
            dividend = -dividend
            sign *= -1
        
        if divisor < 0:
            divisor = -divisor
            sign *= -1
            
        quotient = 0
        
        if divisor == 1:
            quotient = dividend
        else:
            while dividend >= divisor:
                dividend -= divisor
                quotient += 1
            
        ret = quotient * sign
        if ret > 2147483647:
            ret = 2147483647
            
        return ret

#2018-05-17 13:00
#2018-05-17 13:11

class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        sign = -1 if (dividend < 0) ^ (divisor < 0) else 1
        dividend = abs(dividend)
        divisor = abs(divisor)
        
        quotient = 0
        
        while dividend >= divisor:
            temp_dvs = divisor
            cnt = 1
            while temp_dvs < dividend >> 1:
                temp_dvs = temp_dvs << 1
                cnt += cnt
            dividend -= temp_dvs
            quotient += cnt

        quotient = quotient * sign
        if quotient > 2147483647:
            quotient = 2147483647
            
        return quotient
    

if __name__ == "__main__":
    s = Solution()
    
    # 0
    print s.divide(0, 1)
    # 3
    print s.divide(10, 3)
    # -3
    print s.divide(10, -3)
    # -3
    print s.divide(-10, 3)
    # 3
    print s.divide(-10, -3)