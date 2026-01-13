class Solution {
public:
    int minTimeToVisitAllPoints(vector<vector<int>> const& points) {
        auto timeToVisitTwoPoints = [](auto const& p1, auto const& p2) {
            return std::max(std::abs(p1[0] - p2[0]), std::abs(p1[1] - p2[1]));
        };

        int acc = 0;
        for (int i = 1; i < points.size(); ++i) {
            acc += timeToVisitTwoPoints(points[i], points[i - 1]);
        }
        return acc;
    }
};
