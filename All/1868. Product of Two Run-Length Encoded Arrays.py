class Solution:
    def findRLEArray(self, encoded1: List[List[int]], encoded2: List[List[int]]) -> List[List[int]]:
        ptr1, ptr2 = 0, 0
        val1, freq1, val2,freq2 = 0,0,0,0
        result = []
        while ptr1 < len(encoded1) and ptr2 < len(encoded2):
            #print("ptr1 = ",ptr1)
            #print("ptr2 = ",ptr2)
            if freq1 == 0 and freq2 == 0:
                val1, freq1 = encoded1[ptr1]
                val2, freq2 = encoded2[ptr2]
            else:
                if freq1 == 0:
                    val1, freq1 = encoded1[ptr1]
                else:
                    val2, freq2 = encoded2[ptr2]
            prod = val1 * val2
            freq = min(freq1,freq2)
            freq1 -= freq
            freq2 -= freq
            if freq1:
                ptr2 += 1
            elif freq2:
                ptr1 += 1
            else:
                ptr1+= 1
                ptr2 += 1
            if not result or result[-1][0] != prod:
             #   print("Result 1 = ",result)
              #  print("prod = ",prod)
               # print("Freq = ",freq)
                result.append([prod,freq])
            else:
                #print("Result = ",result)
                #print("Freq = ",freq )
                result[-1][1] += freq
            
            
        return result
        
                
