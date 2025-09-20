# 9. Palindrome Number

from collections import deque

# Solution using deque
class SolutionDeque:
    def isPalindrome(self, x: int) -> bool:
        d = deque(str(x))
        while len(d)>=2:
            if d.pop() != d.popleft():
                return False
        return True

# Solution using slicing
class SolutionSlice:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        return s == s[::-1]
    
# Test cases
if __name__ == "__main__":
    x = 121
    print(SolutionDeque().isPalindrome(x))
    print(SolutionSlice().isPalindrome(x))