class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        n = len(routes)
        bus_stops = {}
        for i, route in enumerate(routes):
            for stop in route: 
                if stop not in bus_stops:
                    bus_stops[stop] = set()
                bus_stops[stop].add(i)
        
        if target not in bus_stops:
            return -1
        if target == source:
            return 0
        
        graph = []
        for _ in range(n):
            graph.append(set())

        for stop in bus_stops:
            route_inds = bus_stops[stop] # ind of route that go to this stop=

            for r1 in route_inds:
                for r2 in route_inds:
                    if r1 == r2:
                        continue 

                    graph[r1].add(r2)
                    graph[r2].add(r1)
        
        stop_inds = set(bus_stops[target])
        start_inds = bus_stops[source]

        print(start_inds, stop_inds)

        q = start_inds

        num_transfers = 0
        visited = set()
        while len(q):
            new_q = []
            for rind in q:
                if rind in visited:
                    continue

                visited.add(rind)
                if rind in stop_inds:
                    return num_transfers + 1

                for r2ind in graph[rind]:
                    new_q.append(r2ind)

            num_transfers += 1
            q = new_q
            
        return -1
