class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        set_list = []
        grouping = []
        for str in strs:
            str_to_set = sorted(list(str))
            if str_to_set in set_list: grouping[set_list.index(str_to_set)].append(str)
            else: 
                set_list.append(str_to_set)
                grouping.append([str])
        return grouping