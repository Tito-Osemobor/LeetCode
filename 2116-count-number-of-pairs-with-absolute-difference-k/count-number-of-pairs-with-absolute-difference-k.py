class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        count = 0
        i = 0
        j = len(nums) - 1
        nums.sort()
        while(i < len(nums)):
            if abs(nums[j] - nums[i]) == k:
                count += 1
                j -= 1
            elif abs(nums[j] - nums[i]) < k:
                i += 1
                j = len(nums) - 1
            else:
                j -= 1
        return count