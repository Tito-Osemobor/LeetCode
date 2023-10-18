/**
 * @param {string[]} sentences
 * @return {number}
 */
var mostWordsFound = function(sentences) {
    let count = 0;
    for (let i = 0; i < sentences.length; i ++) {
    let currentCount = 1;
        for (let j = 0; j < sentences[i].length; j ++) {
            if (sentences[i][j] === " ") {
                currentCount ++;
            }
        }
        if (currentCount > count) {
            count = currentCount;
        }
    }
    return count;
};