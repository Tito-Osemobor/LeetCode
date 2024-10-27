class Solution:
    def maxArea(self, height: List[int]) -> int:
        pointer1, pointer2 = 0, len(height) - 1
        max_area = 0
        while pointer1 < pointer2:
            new_area = min(height[pointer1], height[pointer2]) * (pointer2 - pointer1)
            max_area = max(new_area, max_area)
            if height[pointer1] < height[pointer2]:
                pointer1 += 1
            else:
                pointer2 -= 1
        return max_area