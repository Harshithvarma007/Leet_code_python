from collections import defaultdict

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        grouping = defaultdict(list)

        for word in strs:
            # Sort the characters in the word to create a unique key
            sorted_word = ''.join(sorted(word))
            
            # Add the word to the group identified by the sorted key
            grouping[sorted_word].append(word)

        # Convert the defaultdict to a list of lists
        result = list(grouping.values())
        return result
