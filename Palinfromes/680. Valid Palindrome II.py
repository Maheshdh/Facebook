class Solution:
    def isPalindrome(self,str_input):
        return str_input == str_input[::-1]

    def validPalindrome(self, s: str) -> bool:
        if not s:
            return True
        left_char, right_char = 0,len(s)-1
        while left_char<=right_char:
            if(s[left_char] == s[right_char]):
                left_char+=1
                right_char-=1
            else:
                return self.isPalindrome(s[left_char+1:right_char+1]) or self.isPalindrome(s[left_char:right_char])
        return True    


        
