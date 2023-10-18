/**
 * @param {number[]} nums
 * @return {number[]}
 */
var getConcatenation = function(nums) {
    let ans = nums;
    let length = nums.length
    for (let i = 0; i < length; i ++) {
        ans[i + length] = nums[i];
    }
    return ans;
};