class Solution:
    def categorizeBox(self, length: int, width: int, height: int, mass: int) -> str:

        heavy = mass >= 100

        bulky = length >= 10 ** 4 or width >= 10 ** 4 or height >= 10 ** 4 or length * width * height >= 10 ** 9

        if heavy and bulky:
            return "Both"
        elif heavy:
            return "Heavy"
        elif bulky:
            return "Bulky"

        return "Neither"
            
