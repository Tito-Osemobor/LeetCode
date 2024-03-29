class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        sum = nums[0]
        for a,b in pairwise(nums):
            if b == a+1:
                sum += b
            else:
                break
        while sum in nums:
            sum += 1
        return sum
        