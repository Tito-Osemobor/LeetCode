/**
 * @param {number[]} encoded
 * @param {number} first
 * @return {number[]}
 */
var decode = function(encoded, first) {
    const length = encoded.length;
    let ans = [first];
    for (let i = 0; i < length; i ++) {
        ans.push(encoded[i] ^ ans[i]);
    }
    return ans;
};