# @param {Integer[]} nums
# @return {Integer}
def array_pair_sum(nums)
    nums.sort.select.with_index{|_,i| i % 2 == 0}.inject(0, :+)
end