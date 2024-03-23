class Solution:
    def simplifyPath(self, path: str) -> str:
        sub_dirs = path.split("/")
        stack = []
        for directory in sub_dirs:
            if directory == ".":
                continue
            elif directory == "..":
                if stack:
                    stack.pop()
            else:
                if directory != "":
                    stack.append(directory)
        print("Stack = ",stack)
        result = "/".join(stack)
        #print(result)
        return "/" + "/".join(stack)
        
