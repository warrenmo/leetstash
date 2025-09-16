#include <numeric>


class Solution {
public:
    std::vector<int> replaceNonCoprimes(const std::vector<int>& nums) {
        auto res { std::vector<int>{} };
        for (int num : nums) {
            while (true) {
                int gcd = std::gcd(num, (res.empty() ? 1 : res.back()));
                if (gcd == 1) break;
                num *= res.back() / gcd;
                res.pop_back();
            }
            res.push_back(num);
        }
        return res;
    }
};

