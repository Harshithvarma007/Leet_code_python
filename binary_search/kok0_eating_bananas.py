class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        def can_finish(speed):
            hours_required=0
            for pile in piles:
                hours_required+=(pile+speed-1)//speed
            return hours_required<=h

        left,right=1,max(piles)
        while(left<right):
            mid=left+(right-left)//2
            if can_finish(mid):
                right=mid
            else:
                left=mid+1
        return left
           


        

        