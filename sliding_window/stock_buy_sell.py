class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_profit=0
        left,right=0,1
        while left<=right and right <len(prices):
            if prices[right]>=prices[left]:
                max_profit=max(max_profit,prices[right]-prices[left])
                right+=1
            elif prices[right]<prices[left]:
                left=right
                right+=1
        return max_profit
                





        