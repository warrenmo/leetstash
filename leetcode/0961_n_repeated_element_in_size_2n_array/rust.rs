impl Solution {
    pub fn repeated_n_times(nums: Vec<i32>) -> i32 {
        if nums[0] == nums[2] || nums[0] == nums[3] { return nums[0]; }
        if nums[1] == nums[3] { return nums[1]; }

        for window in nums.windows(2) {
            if window[0] == window[1] { return window[0]; }
        }

        // unreachable
        -1
    }
}
