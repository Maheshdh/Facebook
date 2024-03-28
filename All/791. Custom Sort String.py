class Solution:
    def customSortString(self, order: str, s: str) -> str:
        s_counts = collections.Counter(s)
        result = []
        for char in order:
            if char in s_counts:
                count = s_counts[char]
                for qty in range(count):
                    result.append(char)
                s_counts[char] = 0
        for remaining_char in s_counts:
            if(s_counts[remaining_char]):
                qty = s_counts[remaining_char]
                for count in range(qty):
                    result.append(remaining_char)
        return "".join(result)
        
