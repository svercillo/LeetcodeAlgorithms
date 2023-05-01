class UndergroundSystem:

    def __init__(self):
        self.customer_checkins = {}
        self.dist = defaultdict(lambda : (0,0))

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.customer_checkins[id] = (stationName, t)
        

    def checkOut(self, id: int, stationName: str, t: int) -> None:

        checkin_station, checkin = self.customer_checkins[id]
        travel_time = t - checkin

        total_time, num_samples = self.dist[(checkin_station, stationName)]


        total_time += travel_time
        num_samples += 1

        self.dist[(checkin_station, stationName)] = (total_time, num_samples)
    
    
    def getAverageTime(self, startStation: str, endStation: str) -> float:
        total_time, num_samples = self.dist[(startStation, endStation)]

        return total_time / num_samples
