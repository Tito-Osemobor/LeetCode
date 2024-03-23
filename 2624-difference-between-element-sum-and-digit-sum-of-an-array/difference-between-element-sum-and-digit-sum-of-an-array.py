class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        total = 0
        for i in nums:
            num = str(i)
            total += sum(int(digit) for digit in num)
        return abs(sum(nums) - total)