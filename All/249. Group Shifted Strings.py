class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        group_strings = collections.defaultdict(list)
        for string in strings:
            if (len(string) == 1):
                group_strings[(-1,)].append(string)
            else:
                char_diff = []
                for i in range(1,len(string)):
                    char_diff.append((ord(string[i])-ord(string[i-1]))%26)
                group_strings[tuple(char_diff)].append(string)
        return group_strings.values()
        
