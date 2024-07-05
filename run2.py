import datetime
import time
from bisect import bisect_left



class LogSystem:

    def __init__(self):
        self.timestamp_format = '%Y:%m:%d:%H:%M:%S'
        self.events = []

    def convert_to_seconds_since_epoch(self, timestamp_str):
        dt = datetime.datetime.strptime(timestamp_str, self.timestamp_format)
        return time.mktime(dt.timetuple())


    def put(self, id: int, timestamp: str) -> None:
        time_since = self.convert_to_seconds_since_epoch(timestamp)
        self.events.append((time_since, id))
        self.events.sort()
        
    def retrieve(self, start: str, end: str, granularity: str):
        start_ts = self.rewrite_ts(start, granularity)
        end_ts = self.rewrite_ts(end, granularity, False)

        lind = bisect_left(self.events, start_ts)
        rind = bisect_left(self.events, end_ts)

        if not(0 <= lind < rind < len(self.events)):
            return []
        
        

        if self.events[rind] == end_ts:
            rind -= 1
        return self.events[lind:rind]
    
        
    def rewrite_ts(self, ts, granularity, upper:bool=True):
        granularity_rank_map = {"Year" : 5, "Month" : 4 , "Day" : 3, "Hour" : 2, "Minute" : 1, "Second" : 0}
        rank = granularity_rank_map[granularity]

        year = ts[:4] 
        month = ts[5:7]
        day = ts[8:10]
        hour = ts[11: 13]
        minute = ts[14: 16]
        sec = ts[17:]

    
        if rank == 5:
            month = "01"
        if rank >= 4:
            day = "01"
        if rank >= 3:
            hour = "00"
        if rank >= 2:
            minute = "00"
        if rank >= 1: 
            sec = "00"
        if rank >= 0:
            pass

        beginning_ts = f"{year}:{month}:{day}:{hour}:{minute}:{sec}"

        if upper:
            print("START:", beginning_ts)
            return self.convert_to_seconds_since_epoch(beginning_ts)

        dt = datetime.datetime.strptime(beginning_ts, self.timestamp_format)
        if granularity == "Year":
            nxt_dt = dt.replace(year=dt.year + 1)
        elif granularity == "Month":
            if dt.month == "12":
                nxt_dt = dt.replace(year=dt.month + 1).replace(month=1)
            else:
                nxt_dt = dt.replace(month=dt.month)
        elif granularity == "Day":
            nxt_dt = dt + datetime.timedelta(days=1)
        elif granularity == "Hour":
            nxt_dt = dt + datetime.timedelta(hours=1)
        elif granularity == "Minute":
            nxt_dt = dt + datetime.timedelta(minutes=1)
        elif granularity == "Second":
            nxt_dt = dt + datetime.timedelta(seconds=1)

        print("END:", nxt_dt.strftime(self.timestamp_format))
        return time.mktime(nxt_dt.timetuple())

        

LogSystem().retrieve("2016:01:15:01:01:01", "2016:12:31:23:00:00", "Day")