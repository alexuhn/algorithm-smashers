func twoSum(nums []int, target int) []int {
    var result []int
    checked := make(map[int]int)
    
    for index, num := range nums {
        if targetIndex, ok := checked[target - num]; ok {
            result = []int{index, targetIndex}
        }
        checked[num] = index
    }
    return result
}
