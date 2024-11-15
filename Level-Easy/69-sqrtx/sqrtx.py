class Solution:
    def mySqrt(self, x: int) -> int:
        low = 1
        high = x

        while low <= high:
            mid = (low + high) // 2
            if (mid * mid) == x:
                return mid
            elif (mid * mid) > x:
                high = mid - 1
            else:
                low = mid + 1
        return high