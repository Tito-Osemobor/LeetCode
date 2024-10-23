class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums = list(set(nums))

        # If there are less than 3 unique numbers, return the max
        if len(nums) < 3:
            return max(nums)
        
        # Remove the max two times to get the third max
        nums.remove(max(nums))
        nums.remove(max(nums))
        
        return max(nums)  # Now the max is the third largest