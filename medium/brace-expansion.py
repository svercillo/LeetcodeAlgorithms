class Solution:
    def expand(self, s: str) -> List[str]:
        
        
        substr_arr = []
        chars_arr = []
        sub = ""
        chars = ""
        
        processing = True
        
        for i, c in enumerate(s):
            
            if processing:
                if c == "{":
                    chars = ""
                    processing = False
                    substr_arr.append(sub)
                    sub = ""
                else:
                    sub += c
            else: # in between brackets
                if c == "}":
                    chars_arr.append(sorted(chars.split(",")))
                    processing = True
                else:
                    chars += c 
        
        substr_arr.append(sub)
        chars_arr.append([])
        # print(substr_arr)
        # print(chars_arr)
        
        string_size = 0
        for s in substr_arr:
            if len(s) >0:
                string_size += len(s)
            
        for carr in chars_arr:
            if len(carr) > 0:
                string_size += 1
                
                

        res = []
        
        def dfs(curr_str, sub_ind):
            nonlocal substr_arr, chars_arr, res
            
            # print(curr_str, sub_ind, chars_arr[sub_ind])
            
            if len(curr_str) == string_size:
                res.append(curr_str)
            else:
                curr_str += substr_arr[sub_ind]
                
                if len(curr_str) == string_size:
                    res.append(curr_str)
                else:
                    for c in chars_arr[sub_ind]:
                        temp_str ="" + curr_str +c
                        dfs(temp_str, sub_ind + 1)

        dfs("", 0)
        
        return res
