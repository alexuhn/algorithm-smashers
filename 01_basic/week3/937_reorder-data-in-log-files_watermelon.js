/**
 * @param {string[]} logs
 * @return {string[]}
 */
var reorderLogFiles = function(logs) {
    let letterLogs = [];  // Letter-log를 저장할 배열
    let digitLogs = [];  // Digit-log를 저장할 배열
    
    logs.forEach(log => {
        // isNaN() 함수는 string이어도 숫자라면 false 반환
        if (isNaN(log.slice(-1))) {
            letterLogs.push(log.split(' '));
        } else {
            digitLogs.push(log);
        }
    })
    
    // identifier 기준 정렬
    letterLogs.sort((a, b) => {
        return a[0] > b[0] ? 1 : (a[0] < b[0] ? -1 : 0);
    });
    
    // identifier 제외 사전순 정렬
    letterLogs.sort((a, b) => {
        return a.slice(1) > b.slice(1) ? 1 : (a.slice(1) < b.slice(1) ? -1 : 0);
    });
    
    // 리스트를 문자열로 변환하여 재할당
    letterLogs.forEach((element, index, arr) => {arr[index] = element.join(' ');})
    
    return [...letterLogs, ...digitLogs]
    
};
