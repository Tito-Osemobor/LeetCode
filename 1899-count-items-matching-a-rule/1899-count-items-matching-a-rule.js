/**
 * @param {string[][]} items
 * @param {string} ruleKey
 * @param {string} ruleValue
 * @return {number}
 */
var countMatches = function(items, ruleKey, ruleValue) {
    let count = 0;
    const keyIndex = ['type', 'color', 'name'].indexOf(ruleKey);

    items.forEach(element => {
        if (element[keyIndex] === ruleValue) count ++;
    });
    return count;
};