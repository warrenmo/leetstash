impl Solution {
    pub fn plus_one(digits: Vec<i32>) -> Vec<i32> {
        let mut res = digits.to_vec();

        for i in (0..res.len()).rev() {
            if res[i] != 9 {
                res[i] += 1;
                return res;
            }

            res[i] = 0;
        }

        res[0] = 1;
        res.push(0);

        res
    }
}
