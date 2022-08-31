/**
 * @param {string[]} strs
 * @return {string[][]}
 */
var groupAnagrams = function(strs) {
    const group = {};
    
    for (string of strs) {
        let key = [...string].sort();
        key = key.join("");
        
        if (key in group) {
            group[key] = [...group[key], string];
        } else {
            group[key] = [string];
        }
    }
    
    return [...Object.values(group)];
};
