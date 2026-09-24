class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {")": "(", "]": "[", "}": "{"}
        stack = []
        for char in s:
            if char in brackets.values():
                stack.append(char)
            elif char in brackets:
                if not stack:
                    return False
                last_value = stack.pop()
                if brackets[char] != last_value:
                    return False
        if stack:
            return False
        return True