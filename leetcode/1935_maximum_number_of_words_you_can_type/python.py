class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        broken_letters_set = {c for c in brokenLetters}
        return sum(
            all(
                c not in broken_letters_set
                for c in word
            )
            for word in text.split()
        )
