class Solution:
    def calculate(self, s: str) -> int:
        result = 0
        cur_num = 0
        cur_op = "+"
        index = 0
        prev = 0
        while index < len(s):
            if s[index].isdigit():
                while index < len(s) and s[index].isdigit():
                    cur_num = 10 * cur_num + int(s[index])
                    index += 1
                index -= 1

                if cur_op == "+":
                    result += cur_num
                    prev = cur_num
                elif cur_op == "-":
                    result -= cur_num
                    prev = -cur_num
                elif cur_op == "*":
                    result -= prev
                    result += prev * cur_num
                    prev = prev * cur_num
                elif cur_op =="/":
                    result -= prev
                    result += int(prev / cur_num)
                    prev = int(prev/cur_num)
                cur_num = 0
            elif s[index] != " ":
                cur_op = s[index]
            index += 1
        return result

        
