class Solution:
    def miceAndCheese(self, reward1: List[int], reward2: List[int], k: int) -> int:

        n = len(reward1)

        array = []
        for i in range(n):
            array.append((reward1[i], reward2[i], i))

        array.sort(key =lambda k : -(k[0] - k[1]))


        print(array)
        for i in range(k):
            _, _, index = array[i]
            reward1[index] *= -1

        total = 0
        for i in range(n):
            if reward1[i] < 0:
                total += -reward1[i]
            else:
                total += reward2[i]

        return total  
