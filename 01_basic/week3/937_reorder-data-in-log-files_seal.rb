# @param {String[]} logs
# @return {String[]}
def reorder_log_files(logs)
    # 1차시도 - 파이썬 그대로 따라했는데 시간이 2.5배, 메모리는 15배
    logs.each_with_index.sort_by { |log, index| log.split()[-1] =~ /[[:digit:]]/ ? [1, index] : [-1, log.split()[1..-1], log.split()[0]] }.map { |log| log[0] }

    # 2차시도 - 디스커션 참고해봤는데 시간이 반정도 줄어들었다. 메모리는 여전했다.
    def is_alpha?(word)
        word =~ /[[:alpha:]]/ ? true : false
    end

    alpha = []
    numeric = []

    logs.each do |log|
        first_content = log.split(" ")[1] # ["let1", "art", "can"] => "art"
        if is_alpha?(first_content)
            alpha << log
        else
            numeric << log
        end
    end

    alpha.sort_by! do |log|
        identifier, content = log.split(" ", 2) # ["let1", "art can"]
        [content, identifier] # sort by content, then identifier
    end

    return alpha + numeric


    # 3차시도 - 짧게 바꿔보고 싶었지만 시간이 늘어났다.
    # def is_alpha?(word)
    #     word =~ /[[:alpha:]]/ ? true : false
    # end
    # 이 부분을 줄여봤지만 시간이 늘어났다.
    # alpha = logs.map {|log| log.split()[-1] =~ /[[:alpha:]]/ ? log : nil}.compact
    # numeric = logs.map {|log| log.split()[-1] =~ /[[:digit:]]/ ? log : nil}.compact
    # alpha.sort_by! do |log|
    #     identifier, content = log.split(" ", 2) # ["let1", "art can"]
    #     [content, identifier] # sort by content, then identifier
    # end
    # return alpha + numeric
end


# # 참고링크
# 루비 sort_by 함수 : https://ruby-doc.org/core-3.1.2/Enumerable.html#method-i-sort_by
# 루비 정규식 비교 연산자 : https://ruby-doc.org/core-2.6.5/Regexp.html#class-Regexp-label-3D-7E+operator
# 루비 each_with_index와 each.with_index의 비교 : https://negabaro.github.io/archive/rails-each_with_index__each_with_index
# 아주 거지같은 언어라는 것을 알게 되었다. 개 느리고 개 구리다.