class Solution {
public:
    int repeatedNTimes(vector<int> const& nums) {
        if (nums[0] == nums[2] || nums[0] == nums[3])
            return nums[0];
        if (nums[1] == nums[3])
            return nums[1];

        for (auto [left, right] : nums | std::views::adjacent<2>) {
            if (left == right)
                return left;
        }

        // unreachable
        return -1;
    }
};
