/**
 * @param {string} s
 * @param {number[]} indices
 * @return {string}
 */
var restoreString = function(s, indices) {
    let answer = [];
    for (let i = 0; i < indices.length; i ++) {
        answer[indices[i]] = s[i];
    }
    return answer.join("");
};