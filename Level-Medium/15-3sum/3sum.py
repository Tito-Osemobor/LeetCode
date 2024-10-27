class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()  # Sort the array first
        result = []
        
        for i in range(len(nums) - 2):
            # Skip duplicate values for the first element of the triplet
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            # Two-pointer approach for the remaining elements
            left, right = i + 1, len(nums) - 1
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
                
                if current_sum == 0:
                    result.append([nums[i], nums[left], nums[right]])
                    
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    
                    # Move both pointers inward
                    left += 1
                    right -= 1
                
                elif current_sum < 0:
                    # Move left pointer to increase the sum
                    left += 1
                else:
                    # Move right pointer to decrease the sum
                    right -= 1
        
        return result