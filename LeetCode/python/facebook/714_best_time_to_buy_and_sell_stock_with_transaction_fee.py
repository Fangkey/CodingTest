# coding=utf-8

# 2018-05-31 15:15
# 2018-05-31 15:42 wrong

class Solution1(object):
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        if len(prices) <= 1:
            return
        
        start = False
        s = 0
        e = 0
        value = 0
        while e < len(prices) - 1:
            if start == False and prices[e + 1] > prices[e]:
                start = True
                s = e
                e += 1
            elif start == True:
                if prices[e] > prices[e + 1]: 
                    if prices[e] - prices[s] > fee:
                        value += (prices[e] - prices[s] - fee)
                        s = e + 1
                        e += 1
                        start = False
                    else:
                        if prices[s] >  prices[e + 1]:
                            s = e + 1
                            e += 1
                        else:
                            e += 1
                else:
                    e += 1
            else:
                 e += 1
                 
        if prices[e] - prices[s] > fee:
            value += (prices[e] - prices[s] - fee)
            
        return value
            

# 2018-05-31 16:35
# 2018-05-31 16:42

class Solution(object):
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        if len(prices) <= 1:
            return 0
        
        short = 0
        long = -prices[0]
        for i in range(1, len(prices)):
            short = max(short, prices[i] + long - fee)
            long = max(long, short - prices[i])
        return short
    
        
        
if __name__ == "__main__":
    s = Solution()
    
    prices = [1,3,7,5,10,3]
    fee = 3
    # 6
    print s.maxProfit(prices, fee)
    
    prices = [1, 3, 2, 8, 4, 9]
    fee = 2
    # 8
    print s.maxProfit(prices, fee)