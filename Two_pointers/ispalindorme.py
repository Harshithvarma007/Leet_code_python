class Solution(object):
    def isPalindrome(self, s):
        size = len(s)
        i = 0
        j = size - 1

        while i < j:
            while i < j and not s[i].isalnum():
                i += 1

            while i < j and not s[j].isalnum():
                j -= 1

            if s[i].lower() == s[j].lower():
                i += 1
                j -= 1
            else:
                return False

        return True
