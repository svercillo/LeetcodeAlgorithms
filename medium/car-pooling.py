import heapq


class Solution:
    def carPooling(self, trips, capacity: int) -> bool:

        trips.sort(key=lambda trip: trip[1])  # sort by x1
        print(trips)

        trip_capacity = capacity
        heap = []

        for load, x1, x2 in trips:

            # print(x1, x2, trip_capacity, heap)
            trip_capacity -= load
            if len(heap) > 0:

                shortest_end, shortest_load = heapq.heappop(heap)
                skip_put_back = False

                while x1 >= shortest_end:
                    # print("AAAAAAAAAAAA")
                    trip_capacity += shortest_load
                    if len(heap) == 0:
                        skip_put_back = True
                        break

                    shortest_end, shortest_load = heapq.heappop(heap)

                if not skip_put_back:
                    heapq.heappush(
                        heap, (shortest_end, shortest_load)
                    )  # put back on the top of the stack if not removable

                # print("heap", heap)
            if trip_capacity < 0:
                return False

            heapq.heappush(heap, (x2, load))

            # print(heap)

        return True

