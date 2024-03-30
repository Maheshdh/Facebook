# Approach
# try building a string by either considering '(' as part of the result or ignoring it
# for the ')', we can do the same. We can only include it if we have more '(' to it's left
# after building each string, check if it's longer than the previous ones we had, which means, we have removed mininmum paraens
# Time Complexity -> O(2*n)
# Space complexity -> O(n)
class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        self.longest = -1
        self.res = set()
        self.dfs(s,[], 0, 0,0)
        return self.res
    
    def dfs(self,input_str,cur_str,index,left_count,right_count):
        if index >= len(input_str):
            if left_count == right_count:
                if len(cur_str) > self.longest:
                    self.longest = len(cur_str)
                    self.res = set()
                    self.res.add("".join(cur_str))
                elif len(cur_str) == self.longest:
                    self.res.add("".join(cur_str))
        else:
            if input_str[index] == "(":
                cur_str.append('(')
                self.dfs(input_str,cur_str,index+1,left_count+1, right_count)
                cur_str.pop()
                self.dfs(input_str,cur_str,index+1,left_count,right_count)
            elif input_str[index] == ")":
                self.dfs(input_str,cur_str,index+1,left_count,right_count)
                if(left_count > right_count):
                    cur_str.append(')')
                    self.dfs(input_str,cur_str,index+1,left_count,right_count+1)
                    cur_str.pop()
            else:
                cur_str.append(input_str[index])
                self.dfs(input_str,cur_str,index+1,left_count,right_count)
                cur_str.pop()
        
