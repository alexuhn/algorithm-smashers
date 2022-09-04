# @param {String} paragraph
# @param {String[]} banned
# @return {String}
def most_common_word(paragraph, banned)
    result = paragraph.split(//)
            .map { |c| c =~ /[[:alpha:]]/ || c == " " ? c.downcase : " " }
            .join
            .split()
            .select { |word| ! banned.include? word }
            .tally
    # puts result
    result.max_by { |word, cnt| cnt }[0]
end