class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        i=0
        j=len(height)-1
        max_area=0
        while(i<j):
            max_area=max(max_area,self.area(i,j,height))
            if(height[i]<height[j]):
                i+=1
            else:
                j-=1
        return max_area
    def area(self,i,j,height):
        return (j-i)*(min(height[i],height[j]))
        