class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        nums = sorted(nums)
        for i in range(0, len(nums), 2):
            alice = nums[i]
            nums[i] = nums[i+1]
            nums[i+1] = alice
        return nums