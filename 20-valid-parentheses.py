"""
Try use a python list and the deque for the implementation of the Stack
https://www.geeksforgeeks.org/stack-in-python/

"""
from collections import deque


my_string = "{[]}"
# "([)]"
# s = "(]"
# s = "()[]{}"
# s = "()"
# s = "([)]"


def isValid(s: str) -> bool:

    stack = deque()

    brackets = {"(": ")", "[": "]", "{": "}"}

    for letter in s:
        if letter in brackets:
            stack.append(letter)
        else:
            if not stack:
                return False
            last_bracket = stack.pop()
            if letter != brackets[last_bracket]:
                return False

    # return len(stack) == 0
    return not stack  # Seems more Pythonic


print(isValid("]"))