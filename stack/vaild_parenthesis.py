class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        
        # Define a mapping for bracket pairs
        bracket_mapping = {')': '(', '}': '{', ']': '['}

        for char in s:
            if char in bracket_mapping:
                # If the current character is a closing bracket
                # Pop the top element from the stack if it matches the corresponding opening bracket
                top_element = stack.pop() if stack else '#'
                
                if bracket_mapping[char] != top_element:
                    return False
            else:
                # If the current character is an opening bracket, push it onto the stack
                stack.append(char)
        
        # If the stack is empty, all brackets are matched
        return not stack
