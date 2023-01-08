import (
    "fmt" 
)
func shortestDistance(wordsDict []string, word1 string, word2 string) int {
    
    state := 0
    word1ind := 0 
    
    var stored string
    var shortest int
    
    
    shortest = int(^uint(0)  >> 1) 
    
    
    for i, word := range wordsDict{
        if state == 0{
            if word == word1  || word == word2 {
                word1ind = i
                state = 1
                stored = word
            }
        } else if state == 1 {      
            if word == stored {
                state = 1
                word1ind = i
            } else if word == word1 ||  word == word2 { 
                if i - word1ind < shortest {
                    shortest = i - word1ind
                    state = 1
                }
                word1ind = i 
                stored = word
            }
            
        }
    }

    return shortest
    
}
