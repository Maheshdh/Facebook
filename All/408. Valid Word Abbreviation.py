class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        i , j = 0,0
        cur_num = ""
        while i < len(word) and j < len(abbr):
            if(not abbr[j].isdigit()):
                if word[i] != abbr[j]:
                    return False
                else:
                    i += 1
                    j += 1
            else:
                cur_num = ""
                while j<len(abbr) and abbr[j].isdigit():
                    cur_num += abbr[j]
                    j += 1
                if(cur_num[0] == "0"):
                    return False
                steps = int(cur_num)
                i += steps 
        return i == len(word) and j == len(abbr)


        
