/**
 * @param {string} s
 * @return {string}
 */
var longestPalindrome = function(s) {
    let result = s.slice(0, 1);
    
    for (let i = 0; i < s.length; i++) {
        // 홀수 palindrome
        let dx = Math.floor((result.length - 1) / 2) + 1;
        while (
            0 <= i - dx && i + dx < s.length && 
            s.slice(i - dx, i + dx + 1) === s.slice(i - dx, i + dx + 1).split("").reverse().join("")
        ) {
            result = s.slice(i - dx, i + dx + 1);
            dx += 1;
        }
        
        // 짝수 palindrome
        dx = Math.floor((result.length - 2) / 2) + 1;
        while (
            0 <= i - dx && i + dx + 1 < s.length && 
            s.slice(i - dx, i + dx + 2) === s.slice(i - dx, i + dx + 2).split("").reverse().join("")
        ) {
            result = s.slice(i - dx, i + dx + 2);
            dx += 1;
        }
    }
    
    return result;
};
