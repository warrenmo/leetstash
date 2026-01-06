// Definition for a binary tree node.
// #[derive(Debug, PartialEq, Eq)]
// pub struct TreeNode {
//   pub val: i32,
//   pub left: Option<Rc<RefCell<TreeNode>>>,
//   pub right: Option<Rc<RefCell<TreeNode>>>,
// }
// 
// impl TreeNode {
//   #[inline]
//   pub fn new(val: i32) -> Self {
//     TreeNode {
//       val,
//       left: None,
//       right: None
//     }
//   }
// }
use std::rc::Rc;
use std::cell::RefCell;
impl Solution {
    pub fn max_level_sum(root: Option<Rc<RefCell<TreeNode>>>) -> i32 {
        let root = root.unwrap();
        let mut max_sum: i32 = std::i32::MIN;
        let mut min_level: i32 = std::i32::MAX;

        let mut level: Vec<Rc<RefCell<TreeNode>>> = vec![root]; 

        let mut next_level: Vec<Rc<RefCell<TreeNode>>> = Vec::new();

        for curr_level in 1.. {
            if level.is_empty() {
                break;
            }

            let mut curr_sum: i32 = 0;
            next_level.clear();

            for node_rc in level.iter() {
                let node = node_rc.borrow();

                curr_sum += node.val;

                if let Some(left) = node.left.clone() {
                    next_level.push(left);
                }
                if let Some(right) = node.right.clone() {
                    next_level.push(right);
                }
            }

            if curr_sum > max_sum {
                max_sum = curr_sum;
                min_level = curr_level;
            }

            std::mem::swap(&mut level, &mut next_level);
        }

        min_level
    }
}
