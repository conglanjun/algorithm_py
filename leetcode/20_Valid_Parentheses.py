class Solution:
    def isValid(self, s):
        stack = []
        parent_map = {')': '(', ']': '[', '}': '{'}
        for str in s:
            if str not in parent_map:
                stack.append(str)
            elif not stack or parent_map[str] != stack.pop():
                return False
        return not stack

