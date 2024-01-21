class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        # create a list
        stack = []
        # create result array
        res = [0] * len(temperatures)  # Initialize the result array with zeros

        for i in range(len(temperatures)):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                # If the current temperature is higher than the temperature
                # at the top of the stack, update the result for the index
                top = stack.pop()
                res[top] = i - top

            stack.append(i)

        return res
