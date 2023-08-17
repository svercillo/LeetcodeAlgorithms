class Solution:
    def findOriginalArray(self, arr: List[int]) -> List[int]:

      n = len(arr)
      if n % 2 == 1:
        return []

      freq = {}
      for e in arr:
        if e not in freq:
          freq[e] = 0
        
        freq[e] += 1 

      arr.sort()

      n_zeros = 0
      i = 0
      while i < n and arr[i] == 0:
        n_zeros += 1
        i += 1

      if n_zeros % 2 == 1:
        return 

      res = []
      while i < n:
        first = arr[i]
        second = arr[i] * 2

        if freq[first] == 0:
          i += 1
          continue

        if first not in freq or second not in freq or (freq[second] < freq[first]):
          return [] 

        for _ in range(freq[first]):
          res.append(first)

        freq[second] -= freq[first]
        freq[first] = 0
        i += 1


      for e in freq:
        if freq[e] and e != 0:
          return []

      for _ in range(n_zeros // 2):
        res.append(0)
      return  res 



        





