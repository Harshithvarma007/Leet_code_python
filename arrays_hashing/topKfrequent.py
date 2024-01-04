class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        hash_map = {}
        ans = []

        # Count the frequency of each number in nums
        for num in nums:
            if num in hash_map:
                hash_map[num] += 1
            else:
                hash_map[num] = 1

        # Find the top k frequent elements
        for _ in range(k):
            max_key = max(hash_map, key=hash_map.get)
            ans.append(max_key)
            del hash_map[max_key]

        return ans