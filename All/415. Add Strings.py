# Time Complexity -> O(max(n1,n2))
# Space Complexity -> O(max(n1,n2))
# Approach
# iterate from backwards of both the strings
# get the int value by using difference of ascii value of the digit and '0'
# maintain a carry to store carry overs
loop till both strings are processed

class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        result = []
        carry = 0
        p1, p2 = len(num1) -1, len(num2)-1
        while p1 >= 0 or p2 >= 0:
            a = ord(num1[p1]) - ord('0') if p1 >= 0 else 0
            b = ord(num2[p2]) - ord('0') if p2 >=0 else 0
            cur_sum = a + b + carry
            result.append(str(cur_sum % 10))
            carry = cur_sum // 10
            p1 -= 1
            p2 -= 1
        if carry:
            result.append(str(carry))
        return "".join(result[::-1])


        
