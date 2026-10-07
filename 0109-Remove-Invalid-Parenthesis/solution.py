
from traitlets import List

class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        def isValid(string):
            balance = 0

            for char in string:
                if char == '(':
                    balance += 1
                elif char == ')':
                    balance -= 1

                    if balance < 0:
                        return False

            return balance == 0

        queue = [s]
        visited = {s}

        while queue:
            valid_strings = []

            # Check all strings at the current removal level
            for current in queue:
                if isValid(current):
                    valid_strings.append(current)

            # If we found valid strings, this is the minimum removal level
            if valid_strings:
                return list(set(valid_strings))

            # Generate strings by removing one parenthesis
            next_queue = []

            for current in queue:
                for i in range(len(current)):
                    if current[i] not in "()":
                        continue

                    new_string = current[:i] + current[i + 1:]

                    if new_string not in visited:
                        visited.add(new_string)
                        next_queue.append(new_string)

            queue = next_queue

        return [""]