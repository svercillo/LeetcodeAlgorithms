class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        p = paragraph
        
        
        no_punc =  re.sub("[^\w\s]", " ", p)
        
        words = no_punc.split()
        words = [w.lower() for w in words]
        
        
                
        freq = {} 
        
        for w in words: 
            if w not in banned:
                if w not in freq: 
                    freq[w] = 1
                else: 
                    freq[w] +=1 
                    
        m  = 0
        m_word = None
        for w in freq:
            if freq[w] > m: 
                m = freq[w]
                m_word = w
                
                
        
        return m_word
