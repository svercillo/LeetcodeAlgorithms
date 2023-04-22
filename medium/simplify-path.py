class Solution:
    def simplifyPath(self, path: str) -> str:

        tokens = path.split("/")

        directories = []
        for tok in tokens:
            if not len(tok):
                continue 
            
            if tok == "..":
                if len(directories):
                    directories.pop()
            elif tok == ".":
                continue
            else:
                directories.append(tok)

        return '/' + '/'.join(directories)


