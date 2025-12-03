class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        def parsefile(fileinfo): 
            splits = fileinfo.split("(")
            content = splits[1][:-1]
            filename = splits[0]

            return content, filename


        duplicates = defaultdict(list)
        for info in paths:
            carr = info.split(" ")
            base = carr[0]

            for info in carr[1:]:
                content, filename= parsefile(info)
                filepath = base + "/" + filename
                duplicates[content].append(filepath)

        return [group for group in duplicates.values() if len(group) > 1]
                

            
            
