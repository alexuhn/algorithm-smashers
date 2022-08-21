class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        for (i, c) in enumerate(s):
            if i >= len(s) // 2:
                break
            else:
                s[i], s[-1 - i] = s[-1 - i], s[i]
        

        # other solution from me 1
        # for i in range(int(len(s)/2)):
        #     s[i], s[-i - 1] = s[-i - 1], s[i]
        
        # other solution from me 2
        # s[:] = s[::-1]

        # other solution from me3
        for i in range(ceil(len(s) / 2)):
            s[i], s[~i] = s[~i], s[i]

