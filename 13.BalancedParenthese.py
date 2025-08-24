#Day13 Balanced Parentheses Check
def is_balanced(S):
    stack = []
    matching = {')': '(', '}': '{', ']': '['}
    for ch in S:
        if ch in "({[":
            stack.append(ch)
        else:  
            if not stack or stack[-1] != matching[ch]:
                return "NO"
            stack.pop()
    return "YES" if not stack else "NO"
S = input().strip()
print(is_balanced(S))
