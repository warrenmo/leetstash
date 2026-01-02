class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        if nums[0] == nums[2] or nums[0] == nums[3]:
            return nums[0]
        if nums[1] == nums[3]:
            return nums[1]

        for left, right in zip(nums, nums[1:]):
            if left == right:
                return left

        return -1
