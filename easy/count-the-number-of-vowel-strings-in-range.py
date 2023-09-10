class Solution:
    def vowelStrings(self, words: List[str], left: int, right: int) -> int:

        vowels = set(['a', 'e', 'i', 'o','u'])

        presum = []
        p = 0
        for i, word in enumerate(words): 
            if word[0] in vowels and word[-1] in vowels:
                p += 1

            presum.append(p)

        if left == 0:
            num_left = 0
        else:
            num_left = presum[left-1]

        num_right = presum[right]

        return num_right - num_left 
