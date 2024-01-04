class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        
        # Initialize the result array
        result = [1] * n
        
        # Calculate the product of all elements to the left of each element
        product = 1
        for i in range(n):
            result[i] *= product
            product *= nums[i]
        
        # Calculate the product of all elements to the right of each element
        product = 1
        for i in range(n - 1, -1, -1):
            result[i] *= product
            product *= nums[i]
        
        return result