
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:

        import string

        np = paragraph.lower().translate(str.maketrans('', '',  string.punctuation)).split()

        nnp = [x for x in np if x not in banned]

        annp = max(set(nnp), key=nnp.count)

        return annp

# 1번째 시도 실패 -> 스플릿 시 공백기준으로 나눠서 b,b,b,b 등 공백 없는 것을 처리하지 못 함
# translate, str.maketrans 등 이용하여 punctuation없애는 방법 찾아서 씀
# set, count 이용하는 법 찾음

# String maketrans() Parameters
# maketrans() method takes 3 parameters: ex-> maketrans(x[, y[, z]])
# x - If only one argument is supplied, it must be a dictionary.
# The dictionary should contain a 1-to-1 mapping from a single character string to its translation OR a Unicode number (97 for 'a') to its translation.
# y - If two arguments are passed, it must be two strings with equal length.
# Each character in the first string is a replacement to its corresponding index in the second string.
# z - If three arguments are passed, each character in the third argument is mapped to None.

# 걍 ','를 ''로 치환해서 제출은 가능한데 좀 후져보여서 안함

        import string
        import re

        np = re.split(
            " |\\" + "|\\".join(list(string.punctuation)), paragraph.lower())
        nnp = [x for x in np if x not in banned + [""]]
        annp = max(set(nnp), key=nnp.count)

        # print("np=", np,"nnp=", nnp, "annp=", annp)

        return annp

# 이거는 강주현한테 물어봤는데 되긴 되는데 좀 ....


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:

        import string

        nopunc = "".join(
            [" " if i in string.punctuation else i for i in paragraph])

        newp = nopunc.lower().split()
        pwithoutbanned = [x for x in newp if x not in banned]

        return max(set(pwithoutbanned), key=pwithoutbanned.count)

# puctuation 일 때 공백으로 치환하는 것이 유효
