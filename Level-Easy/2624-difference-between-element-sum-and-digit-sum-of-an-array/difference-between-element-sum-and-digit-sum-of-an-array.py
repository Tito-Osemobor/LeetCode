class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        total = 0
        for i in nums:
            total += sum(int(digit) for digit in str(i))
        return abs(sum(nums) - total)