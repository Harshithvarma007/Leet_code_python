class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        hash = {}
        for num in nums:
            if num in hash:
                return True
            else:
                hash[num] = 0
        return False
