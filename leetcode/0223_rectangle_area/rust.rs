impl Solution {
    pub fn compute_area(ax1: i32, ay1: i32, ax2: i32, ay2: i32, bx1: i32, by1: i32, bx2: i32, by2: i32) -> i32 {
        let a_area: i32 = (ax2 - ax1) * (ay2 - ay1);
        let b_area: i32 = (bx2 - bx1) * (by2 - by1);

        let x_overlap: i32 = std::cmp::max(0, std::cmp::min(ax2, bx2) - std::cmp::max(ax1, bx1));
        let y_overlap: i32 = std::cmp::max(0, std::cmp::min(ay2, by2) - std::cmp::max(ay1, by1));
        let overlap_area: i32 = x_overlap * y_overlap;

        a_area + b_area - overlap_area
    }
}
