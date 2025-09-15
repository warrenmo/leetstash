#include <algorithm>
#include <set>
#include <sstream>
#include <string>
#include <string_view>


class Solution {
public:
    int canBeTypedWords(const std::string& text, std::string_view brokenLetters) {
        auto brokenLettersSet {
            std::set<char>(std::begin(brokenLetters), end(brokenLetters))
        };
        auto canBeTyped = [&brokenLettersSet](std::string_view word) {
            return std::ranges::all_of(
                word,
                [&brokenLettersSet](char c){
                    return !brokenLettersSet.contains(c);
                }
            );
        };

        auto iss { std::istringstream(text) };
        auto word { std::string{} };
        auto numWords { 0 };
        while (std::getline(iss, word, ' ')) {
            numWords += canBeTyped(word);
        }
        return numWords;
    }
};
