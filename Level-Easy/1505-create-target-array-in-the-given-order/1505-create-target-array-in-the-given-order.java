class Solution {
    public int[] createTargetArray(int[] nums, int[] index) {
        int[] ans = new int[nums.length];
        ArrayList<Integer> arr = new ArrayList<>();
        for(int i = 0; i < nums.length; i++) {
            arr.add(index[i], nums[i]);
        }
        for(int i = 0; i < arr.size(); i++) {
            ans[i] = arr.get(i);
        }
        return ans;
    }
}