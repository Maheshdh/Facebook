class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if not s:
            return 0
        last_ptr = len(s) -1
        count = 0
        while last_ptr >=0 and s[last_ptr] == " ":
            last_ptr -= 1
        
        while last_ptr >=0 and s[last_ptr] != " ":
            last_ptr -= 1
            count += 1
        return count
        
