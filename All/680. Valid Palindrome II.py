class Solution:
    def isPalindrome(self, s , i, j):
        while i < j:
            if(s[i] != s[j]):
                return False
            i += 1
            j -= 1
        return True

        

    def validPalindrome(self, s: str) -> bool:
        left_ptr, right_ptr = 0 , len(s)-1
        while left_ptr < right_ptr:
            if s[left_ptr] != s[right_ptr]:
                return self.isPalindrome(s,left_ptr,right_ptr-1) or self.isPalindrome(s,left_ptr+1, right_ptr)
            left_ptr += 1
            right_ptr -= 1
        return True
        


        
