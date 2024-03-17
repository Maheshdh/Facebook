class Solution:
    # Time Complexity -> O(n)
    # Space Complexity -> O(1)
    def minAddToMakeValid(self, s: str) -> int:
        # loop through each character
        # if char = '(' we need 1 extra ), 
        # if char = ')' we have a matching pair. If right is more than 0, decrement it by 1
        # else we need an opening '(' , so increment left by 1
        # return left + right
        left, right = 0,0
        for i in s:
            if i == '(':
                right +=1
            else:
                if right > 0:
                    right -= 1
                else:
                    left += 1
        return left + right

        
