class Solution:
    def braceExpansionII(self, expression: str) -> list[str]:
        def parse(i):
            result = set()
            current = {""}

            while i < len(expression) and expression[i] != '}':
                
                if expression[i] == '{':
                    part, i = parse(i + 1)

                elif expression[i] == ',':
                    result.update(current)
                    current = {""}
                    i += 1
                    continue

                else:
                    part = {expression[i]}
                    i += 1

                new_current = set()

                for a in current:
                    for b in part:
                        new_current.add(a + b)

                current = new_current

            result.update(current)

            return result, i + 1

        result, _ = parse(0)

        return sorted(result)