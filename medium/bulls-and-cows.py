class Solution:
    def getHint(self, secret: str, guess: str) -> str:

        _map = {}

        for i, c in enumerate(secret):

            if c not in _map:
                _map[c] = set()

            _map[c].add(i)

        bulls = 0
        cows = 0

        extra = {}
        for i, c in enumerate(guess):
            if c != secret[i]:
                if c not in extra:
                    extra[c] = 0
                extra[c] += 1

        for i, c in enumerate(secret):
            if c == guess[i]:
                bulls += 1
            else:
                if c in extra:
                    extra[c] -= 1
                    if extra[c] == 0:
                        extra.pop(c)
                    cows += 1

        return f"{bulls}A{cows}B"
