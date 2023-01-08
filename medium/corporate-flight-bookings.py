class Solution:
    def corpFlightBookings(self, bookings, n: int):
        
        
        bookings.sort(key = lambda ele: ele[0])
    
        arr = [0] * n
        
        
        blen = len(bookings)

        pop_times = {}
        start_times = {}

        for i,b in enumerate(bookings):
            if b[0] not in start_times:
                start_times[b[0]] = [i]
            else: 
                start_times[b[0]].append(i)
            
            if b[1] not in pop_times:
                pop_times[b[1]] = [i]
            else: 
                pop_times[b[1]].append(i)

            
        seats = 0 

        ind = 1
        while ind < bookings[0][0]: 
            ind +=1


        while ind <= n:
            
            if ind in start_times: 
                for k in start_times[ind]:
                    seats += bookings[k][2]
            
                
            arr[ind-1] += seats
            

            if ind in pop_times:
                for k in pop_times[ind]:
                    seats -= bookings[k][2]

            ind +=1 
            
        return arr
