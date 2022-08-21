# 1번 풀이 - range operator
def reverse_string(s)
    # [ruby operator](https://www.tutorialspoint.com/ruby/ruby_operators.htm)
    # ..는 마지막 요소 포함, ...는 마지막 요소 불포함
    for i in 0...s.length / 2.ceil do
        s[i], s[-1 - i] = s[-1 - i], s[i]
    end
end


# 2번 풀이
def reverse_string(s)
    s.reverse!
end


# 3번 풀이 (discussion 참고) - unary filp operator 'tilde'
# 파이썬에서도 된다
def reverse_string(s)
    return nil if s.empty?

    (s.length / 2).times {|i| s[i], s[~i] = s[~i], s[i]}
end


# 4번풀이 (discussion 참고) - until 사용
def reverse_string(s)
    first = -1
    last = s.length
    
    s[first], s[last] = s[last], s[first] until (first += 1) > (last -= 1)
end
