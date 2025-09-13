#include <string_view>
#include <vector>


class Solution {
public:
    int maxFreqSum(std::string_view s) {
        auto isVowel = [](auto c) {
            // https://stackoverflow.com/questions/47846406/c-fastest-way-to-check-if-char-is-vowel-or-consonant
            return (0x208222 >> (c & 0x1F)) & 1;
        };

        auto max_vowel_freq { 0 };
        auto max_consonant_freq { 0 };
        auto char_count { std::vector<int>(26, 0) };

        for (auto c : s) {
            auto count = ++char_count[c - 'a'];
            auto& curr_max = isVowel(c) ? max_vowel_freq : max_consonant_freq;
            curr_max = std::max(curr_max, count);
        }

        return max_vowel_freq + max_consonant_freq;
    }
}; 
