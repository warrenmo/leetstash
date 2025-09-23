#include <sstream>
#include <string>


class Solution {
public:
    int compareVersion(const std::string& version1, const std::string& version2) {
        auto iss1 { std::istringstream(version1) };
        auto iss2 { std::istringstream(version2) };
        auto v1 { std::string{} };
        auto v2 { std::string{} };

        while (!iss1.fail() || !iss2.fail()) {
            std::getline(iss1, v1, '.');
            std::getline(iss2, v2, '.');

            auto i1 { iss1.fail() ? 0 : std::stoi(v1) };
            auto i2 { iss2.fail() ? 0 : std::stoi(v2) };

            if (i1 < i2) return -1;
            else if (i1 > i2) return 1;
        }

        return 0;
    }
};
