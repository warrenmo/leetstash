VOWELS = {'a', 'e', 'i', 'o', 'u'}

class Solution:
    def maxFreqSum(self, s: str) -> int:
        max_vowel_freq = max_consonant_freq = 0
        char_count = [0] * 26

        for c in s:
            idx = ord(c) - ord('a')
            char_count[idx] += 1
            count = char_count[idx]

            if c in VOWELS:
                max_vowel_freq = max(max_vowel_freq, count)
            else:
                max_consonant_freq = max(max_consonant_freq, count)

        return max_vowel_freq + max_consonant_freq
