# 파이썬에서 제일 빨랐던 알고리즘 루비로 변경함

# @param {String} s
# @return {String}
def longest_palindrome(s)
  def isPalindrome(s)
    s == s.reverse
  end

  if isPalindrome(s) then
    return s 
  end

  max_length = 1
  start = 0
  for i in (1...s.length) do
    one_before = s[i - max_length, max_length + 1]
    two_before = s[i - max_length - 1, max_length + 2]
    if i - max_length - 1 >= 0 && isPalindrome(two_before) then
        start = i - max_length - 1
        max_length += 2
    elsif isPalindrome(one_before) then
        start = i - max_length
        max_length += 1
    end
  end

  return s[start, max_length]
end