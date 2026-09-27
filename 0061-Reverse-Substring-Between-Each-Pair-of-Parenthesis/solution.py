class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = [""]

        for char in s:
            if char == '(':
                stack.append("")

            elif char == ')':
                text = stack.pop()
                reversed_text = text[::-1]
                stack[-1] += reversed_text

            else:
                stack[-1] += char

        return stack[0]