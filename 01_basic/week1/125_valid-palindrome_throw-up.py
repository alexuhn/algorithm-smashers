class Solution:
    def isPalindrome(self, s: str) -> bool:
       
        strings = []
        for char in s:
            if char.isalnum():
                strings.append(char.lower())
       
        length = len(strings)
        
        for i in range(length):
            cnt = length - 1 - i
            if strings[cnt] != strings[i]:
                return False
        return True
                
                
        
            