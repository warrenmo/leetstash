use itertools::Itertools;


impl Solution {
    pub fn maximize_square_hole_area(n: i32, m: i32, h_bars: Vec<i32>, v_bars: Vec<i32>) -> i32 {
        let side: i32 = std::cmp::min(
            Self::biggest_gap(h_bars.into_iter().sorted().collect()),
            Self::biggest_gap(v_bars.into_iter().sorted().collect()),
        );
        side * side
    }

    fn biggest_gap(bars: Vec<i32>) -> i32 {
        let mut curr: i32 = 1;
        let mut gap: i32 = 2;

        for i in 1..bars.len() {
            if (bars[i] == bars[i - 1] + 1) {
                gap = std::cmp::max(gap, 2 + curr);
                curr += 1;
            } else {
                curr = 1;
            }
        }

        gap
    }
}
