class Solution {
    public int[] leftRightDifference(int[] nums) {
        int leftSum = 0, rightSum = 0;
        int[] ans = new int[nums.length];
        for (int i = 0; i < nums.length; i ++) {
            ans[i] = Math.abs(leftSum(nums, i) - rightSum(nums,i));
        }
        return ans;
    }

    public int leftSum(int [] nums, int index) {
        int sum = 0;
        for (int i = index; i > 0; i --) {
            sum += nums[i-1];
        }
        return sum;
    }

    public int rightSum(int [] nums, int index) {
        int sum = 0;
        for (int i = index; i < nums.length - 1; i ++) {
            sum += nums[i+1];
        }
        return sum;
    }
}