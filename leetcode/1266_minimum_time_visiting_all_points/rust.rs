impl Solution {
    pub fn min_time_to_visit_all_points(points: Vec<Vec<i32>>) -> i32 {
        let mut acc = 0;
        for i in 1..points.len() {
            acc += std::cmp::max(
                (points[i][0] - points[i - 1][0]).abs(),
                (points[i][1] - points[i - 1][1]).abs(),
            );
        }
        return acc;
    }
}
