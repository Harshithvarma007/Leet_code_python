class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False

        hash_map = {}
        
        # Increment count for characters in string s
        for letter in s:
            if letter in hash_map:
                hash_map[letter] += 1
            else:
                hash_map[letter] = 1
        
        # Decrement count for characters in string t
        for letter in t:
            if letter in hash_map:
                hash_map[letter] -= 1
            else:
                # If a character in t is not in s, return False
                return False

        # Check if all counts are zero
        for value in hash_map.values():
            if value != 0:
                return False

        return True
