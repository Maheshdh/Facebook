class Solution:
    def findRLEArray(self, encoded1: List[List[int]], encoded2: List[List[int]]) -> List[List[int]]:
        result = []
        ptr1, ptr2 = 0 , 0
        freq1, freq2 = 0,0
        val1, val2 = 0, 0
        while ptr1 < len(encoded1) and ptr2 < len(encoded2):
            if freq1 == 0:
                val1, freq1 = encoded1[ptr1]
            if freq2 == 0:
                val2, freq2 = encoded2[ptr2]
            prod = val1 * val2
            if freq1 < freq2:
                ptr1 += 1
                freq2 -= freq1
                freq1 = 0
            
            elif freq1 > freq2:
                ptr2 += 1
                freq1 -= freq2
                freq2 = 0
            else:
                ptr1 += 1
                ptr2 += 1
                freq1 = 0
                freq2 = 0
            freq = min(freq1,freq2)
            if not result or result[-1][0] != product:
                print("prod 1 = ",prod)
                result.append([product,freq])
                print("Result = ",result)
            else:
                result[-1][1] += freq
        return result

    
        
