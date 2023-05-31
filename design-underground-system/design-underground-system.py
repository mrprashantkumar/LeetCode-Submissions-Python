class UndergroundSystem:

    def __init__(self):
        self.tripTimes = defaultdict(lambda : [0, 0])
        self.checkedInCustomers = defaultdict(lambda : [0, 0])
        
    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.checkedInCustomers[id] = [stationName, t]

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        startStation, startTime = self.checkedInCustomers.pop(id)
        tripTime = t - startTime
        self.tripTimes[(startStation, stationName)][0] += tripTime
        self.tripTimes[(startStation, stationName)][1] += 1

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        totalTime, totalTrip = self.tripTimes[(startStation, endStation)]
        return totalTime / totalTrip


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)