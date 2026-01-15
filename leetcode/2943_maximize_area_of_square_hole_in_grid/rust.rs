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
        let mut start = 1;
        let mut expected_next = 2;
        let mut gap = 1;
        let mut i = 0;

        while i < bars.len() {
            if (bars[i] == expected_next) {
                expected_next += 1;
                gap = std::cmp::max(gap, 1 + bars[i] - start);
                i += 1;
            } else {
                start = bars[i] - 1;
                expected_next = start + 1;
            }
        }

        gap
    }
}
