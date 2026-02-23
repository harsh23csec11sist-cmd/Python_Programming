class Solution:
    """
    Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
    determine if the input string is valid.
    """
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {')': '(', '}': '{', ']': '['}
        for char in s:
            if char in mapping:
                # If closing bracket, top of stack must match
                if not stack or stack[-1] != mapping[char]:
                    return False
                stack.pop()
            else:
                # Opening bracket, push onto stack
                stack.append(char)
        return not stack

# Test cases
if __name__ == "__main__":
    sol = Solution()
    assert sol.isValid("()") == True
    assert sol.isValid("()[]{}") == True
    assert sol.isValid("(]") == False
    assert sol.isValid("([)]") == False
    assert sol.isValid("{[]}") == True
    print("All tests passed.")