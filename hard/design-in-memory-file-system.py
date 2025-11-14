class Blob:
    def __init__(self, isfile, prefix,name):
        self.isfile = isfile 
        self.prefix = prefix 
        self.name = name
        self.childs = {} 
        self.content = ""

    def ls(self):
        if self.isfile:
            return [self.name]
        return sorted([name for name in self.childs])
    
    def append(self, content):
        self.content += content


class FileSystem:
    def __init__(self):
        self.root = Blob(False, "", "")    

    def traverse(self, path): 
        sections = path.split("/")[1:]
        node = self.root
        prefix = "/"
        for section in sections:
            if section not in node.childs:
                node.childs[section] = Blob(False, prefix, section) 

            node = node.childs[section]
            prefix += section + "/"

        return node


    def mkdir(self, path: str) -> None:
        node = self.traverse(path)

    def ls(self, path: str) -> List[str]:
        if path != "/":    
            folderpath = "/".join(path.split("/")[:-1])
            filename = path.split("/")[-1]

            print("LS ", folderpath, filename, path)            
            node = self.traverse(path)
        else: 
            node = self.root

        return node.ls()
        
    def addContentToFile(self, filePath: str, content: str) -> None:
        # return None
        node = self.traverse(filePath)
        node.isfile = True
        node.append(content)

        

    def readContentFromFile(self, filePath: str) -> str:
        # return None
        node = self.traverse(filePath)
        return node.content


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath,content)
# param_4 = obj.readContentFromFile(filePath)
