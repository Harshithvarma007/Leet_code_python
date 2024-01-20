class Solution(object):
    def evalRPN(self, tokens):
        stack = []
        operators = set(['+', '-', '*', '/'])

        for token in tokens:
            if token not in operators:
                # If it's an operand, push it onto the stack
                stack.append(int(token))
            else:
                # If it's an operator, pop the last two operands from the stack
                operand2 = stack.pop()
                operand1 = stack.pop()

                # Perform the operation and push the result back onto the stack
                if token == '+':
                    stack.append(operand1 + operand2)
                elif token == '-':
                    stack.append(operand1 - operand2)
                elif token == '*':
                    stack.append(operand1 * operand2)
                elif token == '/':
                    # Handle division by zero
                    if operand2 == 0:
                        return "Error: Division by zero"
                    # Truncate towards zero (int division)
                    stack.append(int(operand1 / operand2)) if operand1 * operand2 >= 0 else stack.append(-int(abs(operand1) / abs(operand2)))

        # The final result should be the only element in the stack
        return stack[0]

