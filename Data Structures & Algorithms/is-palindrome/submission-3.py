import string
class Solution:
    def isPalindrome(self, s: str) -> bool:
        lower = list(string.ascii_lowercase)
        upper = list(string.ascii_uppercase)
        nums = list(string.digits) # list('0123456789')
        
        word = []
        for c in s:
            if c in lower or c in upper or c in nums:
                word.append(c.lower())

        text = ''.join(word)

        if text == text[::-1]:
            return True

        return False

        