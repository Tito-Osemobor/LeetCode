/**
 * @param {string[]} sentences
 * @return {number}
 */
var mostWordsFound = function(sentences) {
    let newSentences = sentences.map(sentence => sentence.split(" "));
    let maxLength = 0;
    for (let i = 0; i < newSentences.length; i ++) {
        if (newSentences[i].length > maxLength) {
            maxLength = newSentences[i].length;
        }
    }
    return maxLength;
};