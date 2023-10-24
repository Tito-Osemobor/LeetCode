/**
 * @param {string[][]} items
 * @param {string} ruleKey
 * @param {string} ruleValue
 * @return {number}
 */
var countMatches = function(items, ruleKey, ruleValue) {

    const keyIndex = ['type', 'color', 'name'].indexOf(ruleKey);

    return items.filter(e => e[keyIndex] === ruleValue).length;
};