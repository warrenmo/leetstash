class Solution {
public:
    double separateSquares(std::vector<std::vector<int>> const& squares) {
        double l = 0;
        double r = 1e9 + 10;
        double const diff = 1e-5;
        while (l + diff < r) {
            double m = (l + r) / 2;

            if (isBelowLess(squares, m)) l = m;
            else r = m;
        }
        return l;
    }

private:
    bool isBelowLess(std::vector<std::vector<int>> const& squares, double y) {
        double below = 0;
        double above = 0;

        for (auto const& square : squares) {
            double below_vert = std::min(static_cast<double>(square[2]), std::max(0.0, y - square[1]));
            below += below_vert * square[2]; 
            above += (square[2] - below_vert) * square[2]; 
        }

        return below < above;
    };

};
