/*
Let T(i,j) be the max dot product of A[..i] and B[..j]. Then,
T(i,j) = max(
             T(i,j-1),  // don't use the last element of B
             T(i-1,j),  // don't use the last element of A
             A[i]*B[j] + T(i-1,j-1)  // use the last elements of A and B
         )
*/
class Solution {
public:
    int maxDotProduct(vector<int> const& nums1, vector<int> const& nums2) {
        auto const M = nums1.size();
        auto const N = nums2.size();

        std::vector<int> prev(nums2.size() + 1, INT_MIN);
        std::vector<int> curr(nums2.size() + 1, INT_MIN);

        for (int i = 0; i < M; ++i) {
            for (int j = 0; j < N; ++j) {
                curr[j + 1] = std::max(
                    curr[j], // T(i,j-1)
                    std::max(
                        prev[j + 1], // T(i-1,j)
                        nums1[i] * nums2[j] + std::max(0, prev[j]) // A[i]*B[j] + T(i-1,j-1)
                    )
                );
            }
            std::swap(prev, curr);
        }

        return prev.back();
    }
};
