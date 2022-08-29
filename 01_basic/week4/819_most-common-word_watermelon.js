/**
 * @param {string} paragraph
 * @param {string[]} banned
 * @return {string}
 */
var mostCommonWord = function(paragraph, banned) {
    paragraph = paragraph.toLowerCase();

    // g: 대상 문자열 내에서 패턴과 일치하는 모든 문자열을 전역 검색
    paragraph = paragraph.replace(/[^a-zA-Z\s]/g, ' ');
    
    const words = paragraph.split(/\s+/g);
    const wordsCount = {};
    let mostCommonCount = 0;
    let answer = '';
    
    const bannedSet = new Set(banned);
    
    // split 결과로 맨 뒤에 빈 문자열이 생길 수 있으므로 이를 bannedSet에 추가
    bannedSet.add('')  
    
    for (word of words) {
        if (bannedSet.has(word)) continue;
        
        // wordsCount 안에 word가 존재한다면 그 값에서 1만큼 더 큰 수를,
        // 존재하지 않는다면 1을 할당
        wordsCount[word] = wordsCount[word] ? wordsCount[word] + 1 : 1;
        
        if (mostCommonCount < wordsCount[word]) {
            mostCommonCount = wordsCount[word];
            answer = word;
        }
    }
    
    return answer;
};
