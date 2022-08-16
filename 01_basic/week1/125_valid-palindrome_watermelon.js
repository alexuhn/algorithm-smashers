/**
 * @param {string} s
 * @return {boolean}
 */
var isPalindrome = function (s) {
  s = s.toLowerCase(); // 소문자 변환

  // g: 대상 문자열 내에서 패턴과 일치하는 모든 문자열을 전역 검색
  const re = /[a-zA-Z0-9]/g;

  // 일치하는 문자열만 찾아 배열로 변환
  // 이때 일치하는 문자열이 없을 경우 null이 반환되므로 기본값으로 빈 배열 설정
  const convertedPhrase = s.match(re) || [];
  const size = convertedPhrase.length;

  for (let i = 0; i < size / 2; i++) {
    if (convertedPhrase[i] !== convertedPhrase[size - i - 1]) {
      return false;
    }
  }

  return true;
};
