def is_balanced(expression):
    stack = []  # Initialize an empty stack to keep track of opening brackets
    opening_chars = '([{'
    closing_chars = ')]}'
    mapping = {')': '(', '}': '{', ']': '['}  # Mapping of closing brackets to opening brackets
    
    for char in expression:
        if char in opening_chars:
            stack.append(char)  # If character is an opening bracket, push it onto the stack
        elif char in closing_chars:
            # If character is a closing bracket
            if not stack or stack[-1] != mapping[char]:
                # If stack is empty or the top of the stack does not match the expected opening bracket
                return False  # Unbalanced expression, return False
            stack.pop()  # Remove the corresponding opening bracket from the stack
    
    # At the end of iteration, if the stack is empty, the expression is balanced
    return len(stack) == 0  # Return True if stack is empty, else return False

# Test the function with sample inputs
expression1 = "([]{})"
expression2 = "([)]"
print(is_balanced(expression1))  # Output: True
print(is_balanced(expression2))  # Output: False
