class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        
        def create_string(words, char_count, maxWidth, last_word=False):


            remaining = maxWidth - char_count 
            print(words, remaining, char_count)
            spaces_per_word = remaining // max((len(words) -1), 1)
            extra_spaces = remaining % max((len(words) -1), 1)

            

            res = "" + words[0]
            for i in range(1, len(words)):

                if not last_word:                        
                    for _ in range(spaces_per_word):
                        res += " "
                    
                    
                    if extra_spaces:
                        res += " "
                        extra_spaces -= 1
                else:
                    res += " "
                
                res += words[i]


            for i in range(len(res), maxWidth):
                res += " "
            
            return res


        fitted_words = []
        row = []
        char_count = 0
        for w in words:
            if char_count + len(row) - 1 + len(w) < maxWidth:
                row.append(w)
                char_count += len(w)
            else:
                fitted_words.append(create_string(row, char_count, maxWidth))
                char_count = len(w)
                row = [w]


        fitted_words.append(create_string(row, char_count, maxWidth, last_word=True))

        return fitted_words
