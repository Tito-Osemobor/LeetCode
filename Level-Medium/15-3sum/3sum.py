class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()  # Sort the array
        result = set()
        
        for i in range(len(nums) - 2):
            left, right = i + 1, len(nums) - 1
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
                
                if current_sum == 0:
                    # Add as a tuple to result set to avoid duplicates
                    result.add((nums[i], nums[left], nums[right]))
                    left += 1
                    right -= 1
                elif current_sum < 0:
                    left += 1
                else:
                    right -= 1
        
        # Convert set of tuples back to list of lists for the expected output format
        return [list(triplet) for triplet in result]