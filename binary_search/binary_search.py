
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        low, high = 0, len(nums) - 1  # Initialize low and high pointers

        while low <= high:  # Continue searching while the search space is not empty
            mid = (low + high) // 2  # Calculate the middle index

            if nums[mid] == target:
                return mid  # Target found, return the index
            elif nums[mid] < target:
                low = mid + 1  # Discard the left half of the search space
            else:
                high = mid - 1  # Discard the right half of the search space

        return -1  # Target not found, return -1
