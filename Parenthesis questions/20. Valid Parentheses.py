class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        for i in s:
            if i in ['(','{','[']:
                st.append(i)
            else:
                if st and ((i == '}' and st[-1] == '{') or (i == "]" and st[-1] == '[') or (i == ')' and st[-1] == '(')):
                    st.pop()
                else:
                    return False
        if st:
            return False
        return True
