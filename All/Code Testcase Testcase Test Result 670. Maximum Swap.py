class Solution:
    def maximumSwap(self, num: int) -> int:
        num_arr = [int(i) for i in str(num)]

        max_id = len(num_arr) - 1
        min_ptr, max_ptr = 0 , 0
        for i in range(len(num_arr)-1,-1,-1):
            if(num_arr[i] > num_arr[max_id]):
                max_id = i
            elif(num_arr[i] < num_arr[max_id]):
                min_ptr = i
                max_ptr = max_id
        num_arr[min_ptr] , num_arr[max_ptr] = num_arr[max_ptr], num_arr[min_ptr]
        return int("".join([str(i) for i in num_arr]))
