class Solution {
public:
    vector<int> plusOne(vector<int> const& digits) {
        vector<int> res(digits);

        for (int i = res.size() - 1; i >= 0; --i) {
            if (res[i] != 9) {
                ++res[i];
                return res;
            }

            res[i] = 0;
        }

        res[0] = 1;
        res.push_back(0);

        return res;
    }
};
