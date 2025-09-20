# 9. Palindrome Number

from collections import deque

class Solution:
    def isPalindrome(self, x: int) -> bool:
        d = deque(str(x))
        while len(d)>=2:
            tmp = d.pop()
            tmp2 = d.popleft()
            if tmp != tmp2:
                return False
        return True
    