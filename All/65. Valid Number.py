class Solution:
    def isNumber(self, s: str) -> bool:
        num_seen = False
        dot_seen = False
        i = 0
        if s[i] in ['+','-']:
            i += 1
        while i < len(s):
            if s[i].isdigit():
                num_seen = True
            elif s[i] == '.':
                if dot_seen:
                    return False
                else:
                    dot_seen = True
            elif s[i] in ["+","-"]:
                return False
            else:
                if not s[i] in ['e',"E"]:
                    return False
                else:
                    if not num_seen:
                        return False
                    else:
                        return self.isvalid(s[i+1:])
            i += 1
        return num_seen
    
    def isvalid(self,sub_str):
        if not sub_str:
            return False
        i = 0
        num_seen = False
        if sub_str[i] in ["+","-"]:
            i += 1
        while i < len(sub_str):
            if sub_str[i] in ['+','-']:
                return False
            if not sub_str[i].isdigit():
                return False
            else:
                num_seen = True
            i += 1
        return num_seen
        
