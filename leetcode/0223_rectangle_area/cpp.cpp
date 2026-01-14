class Solution {
public:
    int computeArea(int ax1, int ay1, int ax2, int ay2, int bx1, int by1, int bx2, int by2) {
        int const a_area = (ax2 - ax1) * (ay2 - ay1);
        int const b_area = (bx2 - bx1) * (by2 - by1);

        int const x_overlap = std::min(ax2, bx2) - std::max(ax1, bx1);
        int const y_overlap = std::min(ay2, by2) - std::max(ay1, by1);
        
        int const overlap_area = std::max(0, x_overlap) * std::max(0, y_overlap);

        return a_area + b_area - overlap_area;
    }
};
