/*
  . e a t
. 0 1 2 3
s 1 2 3 4
e 2 1 2 3
a 3 2 1 2

Let T(i, j) be the minimum ascii delete sum for s1[..i] and s2[..j].
T(i, j) = min(1 + min(T(i-1, j), T(i, j-1)), s1[i] == s2[j] ? T(i-1, j-1) : inf)
*/
#include <numeric>

class Solution {
public:
    int minimumDeleteSum(std::string_view s1, std::string_view s2) {
        std::vector<int> prev(1 + s2.size());
        std::vector<int> curr(1 + s2.size());

        curr[0] = 0;
        auto s2_ascii = s2 | std::views::transform([](auto c){ return static_cast<int>(c); });
        std::partial_sum(std::begin(s2_ascii), std::end(s2_ascii), std::begin(curr) + 1);

        for (int i = 0; i < s1.size(); ++i) {
            std::swap(prev, curr);

            curr[0] = static_cast<int>(s1[i]) + prev[0];

            for (int j = 0; j < s2.size(); ++j) {
                if (s1[i] == s2[j]) {
                    curr[j + 1] = prev[j];
                } else {
                    curr[j + 1] = std::min(
                        static_cast<int>(s1[i]) + prev[j + 1],
                        static_cast<int>(s2[j]) + curr[j]
                    );
                }
            }
        }

        return curr.back();
    }
};
