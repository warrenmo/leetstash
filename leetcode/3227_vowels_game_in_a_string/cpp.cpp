#include <string_view>


class Solution {
public:
    bool doesAliceWin(std::string_view s) {
        auto isVowel = [](char c) {
            // https://stackoverflow.com/questions/47846406/c-fastest-way-to-check-if-char-is-vowel-or-consonant
            return (0x208222 >> (c & 0x1f)) & 1;
        };
        for (auto c : s) {
            if (isVowel(c)) return true;
        }
        return false;
    }
};
