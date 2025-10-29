class Solution:
    def answerString(self, word: str, numFriends: int) -> str:
        if numFriends == 1:
            return word

        lord = -1 
        for c in word:
            lord = max(lord, ord(c))

        n = len(word)
        maxLen = n - numFriends + 1
        starting = []
        for i, c in enumerate(word):
            if ord(c) == lord:
                starting.append(i)
        starting = [(i, i) for i in starting]

        result = (starting[0][0], starting[0][0] + 1)
        while len(starting) and starting[0][1] - starting[0][0] < maxLen:            
            nstarting = []
            mNextOrd = -1
            for start, curr in starting:
                if curr == len(word) -1:
                    continue
                mNextOrd = max(mNextOrd, ord(word[curr+1]))

            for start, curr in starting:
                if curr == len(word) - 1:
                    result = (start, curr + 1)
                    continue

                if ord(word[curr+1]) == mNextOrd: 
                    nstarting.append((start, curr+1))
                    result = (start, curr + 1)

            starting = nstarting
        print(result)

    
        return word[result[0]: result[1]]
                
