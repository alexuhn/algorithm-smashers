class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = collections.defaultdict(list)

        # print(type(anagrams))

        for word in strs:
            anagrams[''.join(sorted(word))].append(word)

        return anagrams.values()

    # dictionary를 제대로 사용해 본 적이 없어서 책 읽고 풀이과정 따라함
    # 5장 dictionary 정의 다시 정독
