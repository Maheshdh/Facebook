class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        stack = []
        prev_time = 0
        result = [0] * n
        for log in logs:
            id , status, time = log.split(":")
            id = int(id)
            time = int(time)
            if status == "start":
                if stack:
                    prev_id = stack[-1]
                    result[prev_id] += time - prev_time
                stack.append(id)
                prev_time = time
            else:
                prev_id = stack.pop()
                result[prev_id] += time - prev_time + 1
                prev_time = time + 1
        return result


        
