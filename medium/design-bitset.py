class Bitset:

    def __init__(self, size: int):
        self.bits = [0] * size
        self.num_ones = 0
        self.n = size
        self.is_flipped = False

    def fix(self, idx: int) -> None:

        if self.bits[idx] == (0 if not self.is_flipped else 1):
            self.bits[idx] = (1 if not self.is_flipped else 0)
            self.num_ones += 1

    def unfix(self, idx: int) -> None:
        if self.bits[idx] == (1 if not self.is_flipped else 0):
            self.bits[idx] = (0 if not self.is_flipped else 1)
            self.num_ones -= 1

    def flip(self) -> None:
        self.is_flipped = not self.is_flipped
        self.num_ones = self.n - self.num_ones
        # print(self.num_ones)

        

    def all(self) -> bool:
        return self.count() == self.n

    def one(self) -> bool:
        return self.count() >= 1

    def count(self) -> int:
        return self.num_ones

    def toString(self) -> str:
        res = []
        for c in self.bits:
            res.append(str((c + (1 if self.is_flipped else 0)) % 2))
    
        return "".join(res)
