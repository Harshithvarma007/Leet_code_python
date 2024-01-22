class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left, right = 0, len(nums) - 1

        while left < right:
            mid = (left + right) // 2

            # Check if mid is the minimum element
            if nums[mid] < nums[right]:
                right = mid
            else:
                left = mid + 1

        # Left will point to the minimum element
        return nums[left]
