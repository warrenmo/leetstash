VOWELS = {'a', 'e', 'i', 'o', 'u'}

class Solution:
    def doesAliceWin(self, s: str) -> bool:
        return any(c in VOWELS for c in s)
