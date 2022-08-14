# @param {String} s
# @return {Boolean}
def is_palindrome(s)
    stack = []
    s.downcase.chars.each do |c|
        stack << c if c.match /[a-zA-Z0-9]/
    end
    
    stack.each_with_index do |c, i|
        return false unless c == stack[-i - 1]
        break if i >= stack.length / 2
    end
    
    true
end


# 검색해서 알아낸 최적 솔루션
def is_palindrome(s)
    s = s.gsub(/[^a-zA-Z\d]/, "").downcase
    s.reverse == s
end

# 훨씬 더 빠른걸 찾음
def is_palindrome(s)
    s = s.downcase.delete("^/a-z0-9/")
    s == s.reverse
end