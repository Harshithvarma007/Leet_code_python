class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hash_map = {}
        answer = []

        for i, num in enumerate(nums):
            complement = target - num

            if complement in hash_map:
                answer.append(hash_map[complement])
                answer.append(i)
                return answer
            else:
                hash_map[num] = i
